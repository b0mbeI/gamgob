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
git clone https://github.com/yourusername/gamgob.git
cd gamgob
chmod +x gamgob.py
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
./gamgob.py -u example.com -w common.txt
                                     

       |\    ______    /|
       │ \ /        \ / │
       \( \_        _/ )/
       _\_, o /  \ o ,_/_
     _(___\___\__/___/___)______________
    │   __│  _  │     │   __│     │ __  │
    │  │  │     │ │ │ │  │  │  │  │ __ ─│
    │_____│__│__│_│_│_│_____│_____│_____│                                 

v0.1
_____________________________________________

URL:                     example.com
Wordlist:                common.txt
_____________________________________________

.bash_history            [Status: 404, Size: 0 bytes, Duration: 151 ms]
.bashrc                  [Status: 404, Size: 0 bytes, Duration: 148 ms]
.cache                   [Status: 404, Size: 0 bytes, Duration: 142 ms]
```

### Options
| Option | Description |
|------|------------|
| `-u`, `--url` | Target URL |
| `-w`, `--wordlist` | Path to wordlist file |
| `-d`, `--delay` | Delay between requests (seconds) |

## License
GAMGOB is licensed under the MIT License. See [License](https://github.com/b0mbeI/gamgob/blob/main/LICENSE)
