def print_results(word, status, size, duration):
    status_str = status
    marker = " [+]" if status == 200 else ""
    size_str = f"{size} bytes"
    duration_str = f"{duration*1000:.0f} ms"
    print(f"{word:<25}[Status: {status_str}, Size: {size_str}, Duration: {duration_str}]{marker}")
    
