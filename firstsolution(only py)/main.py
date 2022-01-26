# version 0.0.4
# author HQXSTICK

from genericpath import exists
from importlib.resources import path
import requests
import re
import os.path
from multiprocessing import Pool
from DecryptLogin import login

headers = {
    'Referer': 'https://music.163.com/',
    "User-Agent": "Chrome/97.0.4692.99"
    # 在这里需要更改你的浏览器配置，下面是一些格式
    # Chrome/Google Chrome 版本
    # Mozilla/Firefox 版本
}


def getlist(id, folder):
    getsongs(id, folder)
    print("\033[33mDONE!\033[0m")
    print("Do you want to download again?(YES or NO) \033[34m", end="")
    conti = input()
    conti.upper()
    while (conti != 'YES') & (conti != 'NO'):
        print("\033[31mERR: invalid option, please try again: \033[0m", end='')
        conti = input()
        conti.upper()
    if conti == 'YES':
        print("\033[32mProgram work again\033[0m", end="\n\n")
        getpath()


def start(id, folder):
    if os.path.isdir(folder):
        getlist(id, folder)
    else:
        os.makedirs(folder)
        getlist(id, folder)


def getpath():
    print("\033[0mplease type your musiclist number here: \033[34m", end="")
    id = input()
    print("\033[0mplease type the way to the folder you want to download (if the path does not exist, it will create it): \033[34m", end="")
    folder = input()
    print("\033[0mdo you want to download more than 10 musics? If yes, you must use your username and your password(YES or NO): \033[34m", end='')
    chose = input()
    chose.upper()
    while (chose != 'YES') & (chose != 'NO'):
        print("\033[31mERR: invalid option, please try again: \033[0m", end='')
        chose = input()
        chose.upper()
    if chose == "YES":
        print("please input your username here: ", end='')
        username = input()
        print("please input your password here: ", end='')
        password = input()
        lg = login.Login()
        infos_return, session = lg.music163(username, password, 'pc')
        start(id, folder)
    elif chose == 'NO':
        start(id, folder)


def getsongs(id, folder):
    playlist_url = "https://music.163.com/playlist?id=%s" % id
    res = requests.get(playlist_url, headers=headers)
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        music_name_url = "https://music.163.com/song?id=%s" % i[0]
        music_html = requests.get(music_name_url, headers=headers)
        music_nam_list = re.findall(
            r'<em class="f-ff2">(.*?)</em>', music_html.text)
        music_name = music_nam_list[0]
        try:
            with open("%s/" % folder+i[1]+'.mp3', 'wb')as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            pass
        except OSError:
            pass
        print("\033[32msuccess download \033[36m", end='')
        print(music_name)


if __name__ == '__main__':
    getpath()
