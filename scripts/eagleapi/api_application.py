# seealso: https://api.eagle.cool/application/info
#
import requests

from . import api_util

def info(server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/application/info

    Returns:
        Response: return of requests.post
    """

    API_URL = f"{server_url}:{port}/api/application/info"

    try:
        r_get = requests.get(API_URL, timeout=(timeout_connect, timeout_read))
    except requests.exceptions.Timeout as e:
        print("Error: api_application.info")
        print(e)
        return

    return r_get

#
# Support function
#
def is_alive(server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    if not port or type(port) != int or port == "":
        port=41595
    try:
        r_get = info(server_url, port, timeout_connect, timeout_read)
    except Exception as e:
        print("Error: api_application.is_alive")
        print(e)
        return False
    try:
        r_get.raise_for_status()
        return True
    except:
        return False

def is_valid_url_port(server_url_port="", timeout_connect=3, timeout_read=3):
    if not server_url_port or server_url_port == "":
        return False
    server_url, port = api_util.get_url_port(server_url_port)
    if not server_url or not port:
        return False
    if not is_alive(server_url=server_url, port=port, timeout_connect=timeout_connect, timeout_read=timeout_read):
        return False
    return True
