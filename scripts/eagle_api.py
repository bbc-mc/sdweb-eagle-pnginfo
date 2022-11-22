# seealso: https://api.eagle.cool/item/add-from-path
#
import requests

def add_from_path(filefullpath, filename, website="", tags:list=[], annotation="", folderId=None):
    """EAGLE API:addFromPath

    Args:
        folderId (str): 13 digit folderId from Eagle.
        filefullpath (str): Full path string of image file. i.e.) C:\test\imgs\test_image.png
        filename (str): Image name
        website (str, optional): Used as "URL" in Eagle UI. Defaults to "".
        tags (list, optional): Used as "tags" in Eagle UI. Defaults to [].
        annotation (str, optional): Used as "memo" in Eagle UI. Defaults to "".

    Returns:
        _type_: _description_
    """

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

    POST_TO = "http://localhost:41595/api/item/addFromPath"

    r_post = requests.post(POST_TO, json=data)

    return r_post
