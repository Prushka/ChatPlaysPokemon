import os
import urllib.request, json

root = "Resources/"
avatart_path = f"{root}web/live2d/bilibili_avatar/"


def if_exists(uid):
    image_file = avatart_path + f"{uid}.jpg"
    if not os.path.isfile(image_file):
        return False
    return True


def fetch_uid(uid):
    uid = str(uid)
    image_file = avatart_path + f"{uid}.jpg"
    if not os.path.isfile(image_file):
        try:
            with urllib.request.urlopen(f"https://api.bilibili.com/x/space/acc/info?mid={uid}", timeout=10) as url:
                data = json.loads(url.read().decode())
                avatar_url = data['data']['face']
                urllib.request.urlretrieve(avatar_url, image_file)
                print(f"[头像获取-成功] UID: {uid} 头像")
        except:
            print(f"[头像获取-失败] UID: {uid} 头像")


def fetch_img_src(uid):
    avatar = "bilibili_avatar/noface.gif"
    if if_exists(uid):
        avatar = f"bilibili_avatar/{uid}.jpg"
    return avatar
