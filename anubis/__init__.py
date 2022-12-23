from httpx import get
from rich import print

def is_good(protocol, proxy, test_site="http://google.com"):
    proxies = {"all://": f"{protocol}://{proxy}"}
    try:
        req = get(test_site, proxies=proxies)
        response_time = req.elapsed.microseconds
        print(f"{proxy} is fine. Ping time {response_time} ms.")
        return proxy, response_time
    except Exception as e:
        print(e)
        return False


def sort_list(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])
