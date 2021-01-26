# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 06:56:44 2021

@author: Lenovo
"""

from typing import Optional, List, Dict, Any
from nonebot.command import CommandSession
from aiocache import cached
from nonebot.experimental.plugin import on_command
from nonebot.plugin import on_natural_language
from nonebot import  IntentCommand
from nonebot.natural_language import NLPSession
import aiohttp
import asyncio
import json

__plugin_name__ = '知乎'

@cached(ttl=5 * 60)
async def get_latest_news() -> Optional[List[Dict[str, Any]]]:
    headers = {'content-type': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.get(DAILY_LATEST_API_URL, headers=headers) as resp:
            payload = json.loads(await resp.read())
    if not isinstance(payload, dict) or 'stories' not in payload:
        return None
    return payload.get('stories') or []


@on_command('zhihu', aliases=('知乎日报'))
async def _(session: CommandSession):
    stories = await get_latest_news()
    if stories is None:
        await session.send('查询失败了......')
    elif not stories:
        await session.send('暂时还没有内容哦')

    reply = ('最新的知乎日报内容如下：\n\n' +
             '\n\n'.join(f'{story["title"]}\n'
                         f'{DAILY_STORY_URL_FORMAT.format(story["id"])}'
                         for story in stories))
    await session.send(reply)


@on_natural_language({'知乎日报'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'zhihu')
