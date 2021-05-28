# -*- coding:utf8 -*-
# -*- author:xiaoxiang -*-

import requests

from bs4 import BeautifulSoup

import datetime

import os


def rtxt():
    response = requests.get(url="https://cn.bing.com/")
    return response.text

def get_image():
    data = datetime.datetime.now()
    soup = BeautifulSoup(rtxt(), "html.parser")
    last_url = soup.find("head").find("link", id="bgLink", href=True).attrs["href"]
    url = f"https://cn.bing.com{last_url}"
    reponse = requests.get(url=url)
    if reponse.status_code != 200:
        print("保存失败*")
        exit()
    print("保存中")
    try:
        with open(f"{data.year}-{data.month}-{data.day}.jpg", "wb") as f:
            f.write(reponse.content)
            print("保存成功")
    except:
        print("保存失败****")
        path = f"{data.year}-{data.month}-{data.day}.jpg"
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    get_image()