# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:41:29 2021

@author: Lenovo
"""

__plugin_name__ = '微博热搜'
from nonebot.command import CommandSession
import aiohttp
import asyncio
import json
from nonebot.experimental.plugin import on_command

URL = 'http://api.hmister.cn/weibo/'

#headers = {
#    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }

async def get_hotsearch():
    async with aiohttp.ClientSession() as client:
        headers = {'content-type': 'application/json'}
        async with client.get(URL,headers = headers) as resp:
            str_json = await resp.read()
            str_json = json.loads(str_json)
    list1 = []
    i = 0
    if str_json.get('code') == 200:
        for data in str_json.get('data'):
            list1.append(data.get('name'))
            i += 1
            if i == 10:
                break
    return list1
    
@on_command('微博',aliases=('微博热搜', '热搜'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session:CommandSession):
    resp =await get_hotsearch()
    str1 = ''
    for item in resp:
        str1 += item + '\n'
    await session.send(str1)