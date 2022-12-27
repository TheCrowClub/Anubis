from httpx import get


def is_good(protocol, proxy, test_site="http://google.com"):
    proxies = {"all://": f"{protocol}://{proxy}"}
    try:
        req = get(test_site, proxies=proxies)
        response_time = req.elapsed.microseconds
        return response_time
    except Exception:
        return False


def sort_list(tuple_list):
    return sorted(tuple_list)
