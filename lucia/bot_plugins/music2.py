# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:57:19 2021

@author: Lenovo
"""

from nonebot.command import CommandSession
from nonebot.message import MessageSegment
from nonebot.experimental.plugin import on_command
from nonebot.command.argfilter import extractors, validators
import asyncio
import aiohttp
import json

__plugin_name__ = '点歌'

QQ_MUSIC_SEARCH_URL_FORMAT = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?g_tk=5381&p=1&n=20&w={}&format=json&loginUin=0&hostUin=0&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&remoteplace=txt.yqq.song&t=0&aggr=1&cr=1&catZhida=1&flag_qc=0'


async def search_song_id(keyword):
    keyword = keyword.strip()
    async with aiohttp.ClientSession() as session:
        async with session.get(QQ_MUSIC_SEARCH_URL_FORMAT.format(keyword),headers={'content-type': 'application/json'}) as resp:
            payload = json.loads(await resp.read())
    try:
        return payload['data']['song']['list'][0]['songid']
    except (TypeError, KeyError, IndexError):
        return None


@on_command('music', aliases=('点歌', '音乐'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def music(session: CommandSession):
    #args = session.current_arg_text.strip(' ',1)
    #if not args[0]:
    keyword = session.get('keyword', prompt='你想听什么歌呢？',
                          arg_filters=[
                              extractors.extract_text,
                              str.strip,
                              validators.not_empty('歌名不能为空哦，请重新发送')
                              ]) 
    #else:
    #    keyword = args[0]
    song_id = await search_song_id(keyword)
    if song_id is None:
        await session.send('没有找到这首歌呢', at_sender=True)
    else :
        await session.send(MessageSegment.music('qq', song_id), at_sender=True)

@music.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['keyword'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的歌曲名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
