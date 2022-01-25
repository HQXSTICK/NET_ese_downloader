# version 1.0.0
# author HQXSTICK
# IT SHOULD BE WORK WITH net_music_downloader.cpp

from genericpath import exists
from importlib.resources import path
import requests
import re
import os
from multiprocessing import Pool
headers = {
    'Referer': 'https://music.163.com/',
    "User-Agent": "Chrome/97.0.4692.99"
    # 在这里需要更改你的浏览器配置，下面是一些格式
    # Chrome/Google Chrome 版本
    # Mozilla/Firefox 版本
}


def getlist(id, folder):
    getsongs(id, folder)
    print("DONE!")
    print("Do you want to download again?(YES or NO) ", end="")
    conti = input()
    if conti == 'YES':
        print("Program work again", end="\n\n")
        getpath()


def getpath():
    print("please type your musiclist number here: ", end="")
    id = input()
    print("please type the way to the folder you want to download: ", end="")
    folder = input()
    getlist(id, folder)


def getsongs(id, folder):
    f = open("out.txt", "w")
    print(folder, file=f)
    playlist_url = "https://music.163.com/playlist?id=%s" % id
    res = requests.get(playlist_url, headers=headers)
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        print(i[0], file=f)
    print(0, file=f)
    f.close()
    downloadpro = "netease_music_downloader_withpyuversion.exe"
    oput = os.popen(downloadpro)
    data = oput.readlines()
    oput.close()


if __name__ == '__main__':
    getpath()
