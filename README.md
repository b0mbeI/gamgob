# GAMGOB
![version](https://img.shields.io/badge/Version-0.1-green) ![Licence](https://img.shields.io/badge/License-MIT-blue)
## Introduction

> Lightweight web enumeration CLI tool written in Python

GAMGOB (a.k.a. Gamma Goblin) is a command-line web enumeration tool designed for low-impact HTTP content discovery.
It performs directory and endpoint enumeration using a wordlist and reports HTTP response
status codes along with response size and request duration.

This tool was created as a learning exercise and does not perform authentication attacks,
password brute forcing, or vulnerability exploitation.<br>
_Use this tool only on systems you own or have explicit authorization to test._

## Installation

Clone the repository and run the script using Python 3:

```bash
git clone https://github.com/b0mbeI/gamgob.git
```

## Usage
> All examples use **example.com**, which is reserved for documentation and testing purposes.

To run GAMGOB, you must specify two required parameters:

- a <b>wordlist</b> containing directory or endpoint names used for enumeration
  - `-w`, `--wordlist` – path to the wordlist file
- a target <b>URL</b>
  - `-u`, `--url`

```
python -m gamgob -u https://example.com -w /path/to/wordlist/wordlist.txt
```


### Example usage
``` 
python -m gamgob -w wordlist.txt -u google.com 
                                     

       |\    ______    /|
       │ \ /        \ / │
       \( \_        _/ )/
       _\_, o /  \ o ,_/_
     _(___\___\__/___/___)______________
    │   __│  _  │     │   __│     │ __  │
    │  │  │     │ │ │ │  │  │  │  │ __ ─│
    │_____│__│__│_│_│_│_____│_____│_____│   

URL:                     google.com
Wordlist:                wordlist.txt
_____________________________________________

test                     [Status: 404, Size: 0 bytes, Duration: 201 ms]
example                  [Status: 404, Size: 0 bytes, Duration: 196 ms]
robots.txt               [Status: 200, Size: 6502 bytes, Duration: 226 ms]
sitemap.xml              [Status: 200, Size: 1717 bytes, Duration: 221 ms]

```

### Options
| Option | Description |
|------|------------|
| `-u`, `--url` | Target URL |
| `-w`, `--wordlist` | Path to wordlist file |
| `-d`, `--delay` | Delay between requests (seconds) |

## License
GAMGOB is licensed under the MIT License. See [License](https://github.com/b0mbeI/gamgob/blob/main/LICENSE)
