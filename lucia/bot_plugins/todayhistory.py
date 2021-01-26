# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:56:40 2021

@author: Lenovo
"""
#+str(data.get('month'))+'月'+str(data.get('day'))+'日'
__plugin_name__ = '历史上的今天'

Appkey = 'c3de2e9cb61d09db2b80d3e10efe5dc3'

URL = 'http://api.juheapi.com/japi/toh?key={}&v=1.0&month={}&day={}'

#headers ={
#    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }
headers = {'content-type': 'application/json'}
from nonebot.command import CommandSession
from datetime import datetime
import pytz
import aiohttp
import asyncio
import json
from nonebot.experimental.plugin import on_command

async def get_msg():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(Appkey,now.month,now.day) , headers = headers) as resp:
            str_json = json.loads(await resp.read())
    event = []
    if str_json.get('reason') == '请求成功！':
        for data in str_json.get('result'):
            str1 = ''
            str1 += str(data.get('year'))+'年'+data.get('title')
            event.append(str1)
    list1 = []
    i=1
    while i<=12:
        list1.append(event[-i])
        i+=1
    return list1
@on_command('历史上的今天',permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session:CommandSession):
    reps = await get_msg()
    str2 = ''
    for item in reps:
        str2 += item+'\n'
    await session.send(str2)
            