import os
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
