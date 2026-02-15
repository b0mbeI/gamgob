import argparse
import time
import sys
from urllib.parse import urljoin
from gamgob.config import logo
from gamgob.input import load_wordlist
from gamgob.results import print_results, json_output
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
    parser.add_argument(
        "-sv", "--save",
        required=False,
        help="save results to JSON file"
        )
    parser.add_argument(
        "-fr", "--filter",
        type = int,
        help="show ony specific HTTP status code (e.g. 200)"
    )
    
    args = parser.parse_args()  
    time.sleep(0.5)
    logo()
    
    print(f"{'URL:':<25}{args.url}")
    print(f"{'Wordlist:':<25}{args.wordlist}")
    print(f"\n" + "-"*45)
    print()
    
    time.sleep(1)
    
    words = load_wordlist(args.wordlist)
    total_words = len(words)
    total_duration = 0
    filename = args.save
    base_url = args.url
    http_sum = 0
    results = []

    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url
    if not base_url.endswith("/"):
        base_url += "/"
    
    for i, word in enumerate(words, start=1):
        target = urljoin(base_url, word)
        status, size, duration = http_check(target)
        if args.filter and status != args.filter:
            continue
        total_duration += duration
        if status == 200:
            http_sum += 1
        results.append({
             "word": word,
             "url": target,
             "status": status,
             "size": size,
          })      
        sys.stdout.write("\r\033[2K")
        
        print_results(word, status, size, duration)
        
        progress_line = f"Progress: {i}/{total_words} | Duration: {total_duration:.2f}s"
      
        sys.stdout.write(progress_line)
        sys.stdout.flush()
   
        if args.delay > 0:
            time.sleep(args.delay)
   
    sys.stdout.write("\r\033[2K")
    
    print(f"\n" + "-"*45)
    print()
    print(f"Scan completed.")
    print(f"[ ] HTTP 200 found : {http_sum}/{total_words}")
    print(f"[ ] Total duration : {total_duration:.2f}s")
    print()
    if args.save:
        json_output(filename, results)
