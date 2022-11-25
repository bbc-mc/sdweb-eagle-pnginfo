# seealso: https://api.eagle.cool/item/add-from-path
#
import requests

def add_from_path(filefullpath, filename, website="", tags:list=[], annotation="", folderId=None, server_url="http://localhost", port=41595):
    """EAGLE API:addFromPath

    Args:
        folderId (str): 13 digit folderId from Eagle.
        filefullpath (str): Full path string of image file. i.e.) C:\test\imgs\test_image.png
        filename (str): Image name
        website (str, optional): Used as "URL" in Eagle UI. Defaults to "".
        tags (list, optional): Used as "tags" in Eagle UI. Defaults to [].
        annotation (str, optional): Used as "memo" in Eagle UI. Defaults to "".
        server_url (str, optional): Eagle Local Server URL with Port. Defaults to "http://localhost:41595"

    Returns:
        Response: return of requests.post
    """
    API_URL = f"{server_url}:{port}/api/item/addFromPath"

    data = {
        "path": filefullpath, #"C://Users/User/Downloads/test.jpg",
        "name": filename #"アルトリア･キャスター",
    }
    if website and website != "":
        data.update({
            "website": website #"https://www.pixiv.net/artworks/83585181",
        })
    if tags and len(tags) > 0:
        data.update({
            "tags": tags #["FGO", "アルトリア・キャスター"],
        })
    if annotation and annotation != "":
        data.update({
            "annotation": annotation #"久坂んむり",
        })
    if folderId:
        data.update({
            "folderId": folderId #"KEHB8I2C9F23H"
        })

    res = requests.post(API_URL, json=data)

    return res
