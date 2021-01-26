# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:53:19 2021

@author: Lenovo
"""

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot.message import MessageSegment
import aiohttp
import asyncio
import aiofiles
import random


__plugin_name__ = 'setu'
__plugin_usage__ = '用法： 对我说 "图片"，我会回复 "发送图片"'

async def get_Pic():

    url = "http://api.mtyqx.cn/api/random.php"

    #headers = {
    #    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    #    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as req:
            content = await req.read()
            path = "D:\\luciabot\\useless\\setu\\{}.jpg".format(str(random.randrange(1,100000)))
            async with aiofiles.open(path, "wb") as f:
                await f.write(content)
    return path


@on_command('setu', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    path = await get_Pic()
    file='file:///' + path
    seq = MessageSegment(type_='image',data={'file':file, 'destruct':'0'})
    await session.send(seq)