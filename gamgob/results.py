import json
from datetime import datetime

def print_results(word, status, size, duration):
    status_str = status
    marker = " [+]" if status == 200 else ""
    size_str = f"{size} bytes"
    duration_str = f"{duration*1000:.0f} ms"
    print(f"{word:<25}[Status: {status_str}, Size: {size_str}, Duration: {duration_str}]{marker}")
    
def json_output(filename, results):
    date = datetime.now().strftime("%Y-%m-%d")
    jsonfile = (f"{filename}_{date}.json")
    with open(jsonfile, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {jsonfile}")
