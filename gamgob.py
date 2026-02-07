import argparse
from importlib.resources import contents
import os
import time
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

version = "0.1"
default_headers = {
    "User-Agent": f"GAMGOB/{version}"
    }

def output_banner():
    banner = r"""                                     

       |\    ______    /|
       │ \ /        \ / │
       \( \_        _/ )/
       _\_, o /  \ o ,_/_
     _(___\___\__/___/___)______________
    │   __│  _  │     │   __│     │ __  │
    │  │  │     │ │ │ │  │  │  │  │ __ ─│
    │_____│__│__│_│_│_│_____│_____│_____│                                 
"""
    print(banner)
    print(f"v0.1\n_____________________________________________\n")

def http_check(url):
    d = time.perf_counter()
    try:
        request = Request(url, method="GET", headers=default_headers)
        with urlopen(request, timeout=10) as req:
            size = int(req.headers.get("Content-Length", 0))
            duration = time.perf_counter() - d
            return req.status, size, duration
    except HTTPError as error:
        duration = time.perf_counter() - d
        return error.code, 0, duration
    except URLError:
        duration = time.perf_counter() - d
        return None, 0, duration

def load_wordlist(path):
    if not os.path.isfile(path):
        print(f"[-] wordlist not found: {path}")
        exit(1)

    with open(path, "r", encoding="utf-8", errors="ignore") as p:
        result = []
        for line in p:
            if line.strip() and not line.startswith("#"):
                result.append(line.strip())
        return result

def print_results(word, status, size, duration):
    status_str = status
    size_str = f"{size} bytes"
    duration_str = f"{duration*1000:.0f} ms"
    print(f"{word:<25}[Status: {status_str}, Size: {size_str}, Duration: {duration_str}]")
    
def main():
    parser = argparse.ArgumentParser(
        description="GAMGOB - web enumeration tool"
        )
    parser.add_argument(
        "-w", "--wordlist",
        required=True,
        help="path to the wordlist"
        )
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="target url"
        )
    parser.add_argument(
        "-d", "--delay",
        type = float,
        default = 1,
        help="delay between requests in seconds"
        )
    
    args = parser.parse_args()  
    time.sleep(0.5)
    output_banner()
    
    print(f"{'URL:':<25}{args.url}")
    print(f"{'Wordlist:':<25}{args.wordlist}")
    print(f"_____________________________________________\n")
    
    time.sleep(1)
    
    words = load_wordlist(args.wordlist)

    base_url = args.url
    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url
    if not base_url.endswith("/"):
        base_url += "/"
    for word in words:
        target = urljoin(base_url, word)
        status, size, duration = http_check(target)
        print_results(word, status, size, duration)
        if args.delay > 0:
            time.sleep(args.delay)

if __name__ == "__main__":
    main()
