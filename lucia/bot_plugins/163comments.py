# -*- coding: utf-8 -*-
#headers = {
#    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }
headers = {'content-type': 'application/json'}
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import json
import aiohttp
import asyncio

async def get_comment():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers = headers) as html:        
            str_json = json.loads(await html.read())
    comment = {}
    if str_json.get('code') == 200:
        comment['name'] = str_json.get('name')
        comment['artist'] = str_json.get('artists_name')
        comment['comment'] = str_json.get('comments')
    return comment

@on_command('热评', aliases=('网易云热评','网易云评论'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session:CommandSession):
    req = await get_comment()
    if (req == None ) or (req['comment'] == None):
        await session.send('获取热评失败')
    else:
        ans = req['comment']+'\n———'+'《'+req['name']+'》'+req['artist']
        await session.send(ans)
