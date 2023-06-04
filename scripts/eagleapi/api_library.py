# see also https://api.eagle.cool/library/info
# see also https://api.eagle.cool/library/switch
#
import json
import requests

def info(server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/library/info

    Method: GET

    Returns:
        list(response dict): return list of response.json()
    """
    API_URL = f"{server_url}:{port}/api/library/info"
    r_get = requests.get(API_URL, timeout=(timeout_connect, timeout_read))
    return r_get

def switch(librarypath, server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/library/switch

    Method: POST

    Returns:
        list(response dict): return list of response.json()
    """
    data = {
        "libraryPath": librarypath
    }
    API_URL = f"{server_url}:{port}/api/library/switch"
    # Convert [dict -> json(str) -> dict], Because of escape text.
    data_escaped = json.loads(json.dumps(data, ensure_ascii=False))
    r_post = requests.post(API_URL, json=data_escaped, timeout=(timeout_connect, timeout_read))
    return r_post
