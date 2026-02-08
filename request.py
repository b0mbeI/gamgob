import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from gamgob.config import HEADER

def http_check(url):
    d = time.perf_counter()
    try:
        request = Request(url, method="GET", headers=HEADER)
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
