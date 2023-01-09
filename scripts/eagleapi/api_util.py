import requests
import ipaddress
from urllib.parse import urlparse

from . import api_folder

def get_url_port(server_url_port=""):
    if not server_url_port or server_url_port == "":
        return None, None
    o = urlparse(server_url_port)
    _url = f"http://{o.hostname}"
    if o.hostname != "localhost":
        _ip = ipaddress.ip_address(o.hostname)
        if _ip.version == 6:
            _url = f"http://[{o.hostname}]"
    port = o.port
    return _url, port

# util for /api/folder/list
def findFolderByID(r_posts, target_id):
    return findFolderByName(r_posts, target_id, findByID=True)

def findFolderByName(r_posts, target_name, findByID=False):
    _ret = []
    if not target_name or target_name == "" or not r_posts:
        return None
    _all_folder = getAllFolder(r_posts)
    for _data in _all_folder:
        if (findByID and _data.get("id", "") == target_name) or (_data.get("name", "") == target_name):
            _ret = _data
            break
    return _ret

def getAllFolder(r_posts):
    """ get dict of {"folderId": _data, ..."""
    def dig_folder(data, dig_count, dig_limit=10):
        dig_count+=1
        if(dig_count>dig_limit):
            return []
        _ret = [data]
        if "children" in data and len(data["children"]) > 0:
            for _child in data["children"]:
                _ret += dig_folder(_child, dig_count)
        return _ret
    _ret = []
    if not r_posts:
        return None
    _posts = r_posts.json()
    if not _posts or "status" not in _posts or _posts["status"] != "success":
        return None
    if "data" in _posts and len(_posts["data"]) > 0:
        for _data in _posts["data"]:
            _ret += dig_folder(_data, 0)
    return _ret

#
# Support functions
#

def print_response(_res:requests.Response):
    print(f"status code : {_res.status_code}")
    print(f"headers     : {_res.headers}")
    print(f"text        : {_res.text}")
    print(f"encoding    : {_res.encoding}")
    print(f"cookies     : {_res.cookies}")

    print(f"content     : {_res.content}")
    print(f"content decode: {_res.content.decode(encoding=_res.apparent_encoding)}")

def get_json_from_response(_res:requests.Response):
    try:
        _result = _res.json()
        return _result
    except:
        return _res

def find_or_create_folder(folder_name_or_id, allow_create_new_folder=False, server_url="http://localhost", port=41595, timeout_connect=3, timeout_read=10):
    """
    Find or Create folder on Eagle, by folderId or FolderName

    Args:
        folder_name_or_id (str):
        allow_create_new_folder (bool, optional): if True, create new folder on Eagle. Defaults to False.
        server_url (str, optional): Defaults to "http://localhost".
        port (int, optional): Defaults to 41595.
        timeout_connect (int, optional): Defaults to 3.
        timeout_read (int, optional): Defaults to 10.
    Return:
        folderId or ""

    """
    _eagle_folderid = ""
    if folder_name_or_id and folder_name_or_id !="":
        _ret_folder_list = api_folder.list(server_url=server_url, port=port, timeout_connect=timeout_connect, timeout_read=timeout_read)

        # serach by name
        _ret = findFolderByName(_ret_folder_list, folder_name_or_id)
        if _ret and len(_ret) > 0:
            _eagle_folderid = _ret.get("id", "")
        # serach by ID
        if _eagle_folderid == "":
            _ret = findFolderByID(_ret_folder_list, folder_name_or_id)
            if _ret and len(_ret) > 0:
                _eagle_folderid = _ret.get("id", "")
        if _eagle_folderid == "":
            if allow_create_new_folder: # allow new
                _r_get = api_folder.create(folder_name_or_id, server_url=server_url, port=port, timeout_connect=timeout_connect, timeout_read=timeout_read)
                try:
                    _eagle_folderid = _r_get.json().get("data").get("id")
                except:
                    _eagle_folderid = ""
    return _eagle_folderid
