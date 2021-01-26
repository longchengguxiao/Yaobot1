# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 00:19:19 2021

@author: Lenovo
"""

__plugin_name__ = 'joke'
__plugin_usage__ = '用法： 对我说 "笑话"，我会回复 "回答"'
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import time
import requests
import random

def xiaobing(msg):
    uid = '5175429989'
    source = '209678993'
    SUB = '_2A25NA9ueDeRhGeNL7VsV8yzKwzmIHXVuD-XWrDV8PUJbkNANLUzskW1NSOSBA5oIbRA787zNg4wNSq25x2t1qOLe'
    url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
    data = {
        'text': msg,
        'uid': uid,
        'source': source
    }
    headers = {
        'cookie': 'SUB='+SUB,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://api.weibo.com/chat/'
    }
    response = requests.post(url_send, data=data, headers=headers).json()
    sendMsg = response['text']
    while True:
        url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(uid, source)
        response = requests.get(url_get, headers=headers).json()
        getMsg = response['direct_messages'][0]['text']
        if sendMsg == getMsg:
            time.sleep(0.5)
        else:
            return getMsg


@on_command('joke', aliases=('讲个笑话吧','来一个笑话', '笑话', '说一个笑话'))
async def joke(session: CommandSession):
    ku = ['讲个笑话','讲一个笑话', '笑话', '说一个笑话']
    temp = random.randrange(0,4)
    rep = xiaobing(ku[temp])
    await session.send(rep)
