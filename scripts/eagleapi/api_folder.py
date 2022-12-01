# see also https://api.eagle.cool/folder/list
#
import requests
import sys

from . import api_util

def create(newfoldername, server_url="http://localhost", port=41595, allow_duplicate_name=True, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/folder/list

    Method: POST

    Returns:
        list(response dict): return list of response.json()
    """
    API_URL = f"{server_url}:{port}/api/folder/create"

    def _init_data(newfoldername):
        _data = {}
        if newfoldername and newfoldername != "":
            _data.update({"folderName": newfoldername})
        return _data
    data = _init_data(newfoldername)

    # check duplicate if needed
    if not allow_duplicate_name:
        r_post = list()
        _ret = api_util.findFolderByName(r_post, newfoldername)
        if _ret != None or len(_ret) > 0:
            print(f"ERROR: create folder with same name is forbidden by option. [eagleapi.folder.create] foldername=\"{newfoldername}\"", file=sys.stderr)
            return

    r_post = requests.post(API_URL, json=data, timeout=(timeout_connect, timeout_read))
    return r_post


def rename(folderId, newName, server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/folder/rename

    Method: POST

    Returns:
        list(response dict): return list of response.json()
    """
    data = {
        "folderId": folderId,
        "newName": newName
    }
    API_URL = f"{server_url}:{port}/api/folder/rename"
    r_post = requests.post(API_URL, json=data, timeout=(timeout_connect, timeout_read))
    return r_post


def list(server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """EAGLE API:/api/folder/list

    Method: GET

    Returns:
        Response: return of requests.post
    """

    API_URL = f"{server_url}:{port}/api/folder/list"

    r_get = requests.get(API_URL, timeout=(timeout_connect, timeout_read))

    return r_get
