import argparse
import time
from urllib.parse import urljoin
from gamgob.config import logo
from gamgob.input import load_wordlist
from gamgob.results import print_results
from gamgob.request import http_check

def run():
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
    logo()
    
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