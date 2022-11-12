from logging import INFO, basicConfig, info, warning

from httpx import get

basicConfig(level=INFO)


def is_good(protocol, proxy, test_site="http://google.com"):
    proxies = {"all://": f"{protocol}://{proxy}"}
    try:
        req = get(test_site, proxies=proxies)
        response_time = req.elapsed.microseconds
        info(f"{proxy} is fine. Ping time {response_time} ms.")
        return proxy, response_time
    except Exception as e:
        warning(e)
        return False


def sort_list(tuple_list):
    return sorted(tuple_list, key=lambda x: x[1])
