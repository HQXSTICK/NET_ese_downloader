# version 1.0.1
# author HQXSTICK

import requests
import re
from multiprocessing import Pool
headers = {
    'Referer': 'https://music.163.com/',
    "User-Agent": "Chrome/97.0.4692.99 "
    # 在这里需要更改你的浏览器配置，下面是一些格式
    # Chrome/版本
    # Mozilla/版本
}


def getlist():
    print("please type your musiclist number here:")
    id = input()
    print("please type the way to the folder you want to download:")
    folder = input()
    getsongs(id, folder)
    print("success!")
    print("Do you want to continue?(YES or NO)")
    conti =input()
    if conti =='YES':
        getlist()


def getsongs(id, folder):
    playlist_url = "https://music.163.com/playlist?id=%s" % id
    res = requests.get(playlist_url, headers=headers)
    mylog = open('html.html', mode='a', encoding='utf-8')
    print(res.text, file=mylog)
    mylog.close()
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        try:
            with open("%s/" % folder+i[1]+'.mp3', 'wb')as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            pass
        except OSError:
            pass


if __name__ == '__main__':
    getlist()
