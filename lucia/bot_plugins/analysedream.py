# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:47:07 2021

@author: Lenovo
"""

Appkey = '28637cbb640e97276bcae6f0ca459141'

URL = 'http://v.juhe.cn/dream/query?q={}&cid=&full=1&key={}'

#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }
headers = {'content-type': 'application/json'}
import aiohttp
import asyncio
import json
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

async def get_dsp(keyword):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(keyword,Appkey), headers = headers) as req:
            str_json = json.loads(await req.read())
    if str_json.get('reason') == 'successed':
        str1 = ''
        data = str_json.get('result')[0]
        for item in data.get('list'):
            str1+=item+'\n'
    return str1

@on_command('周公解梦',aliases=('梦的解析','解梦'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser,only_to_me=True)
async def dream(session:CommandSession):
    args = session.current_arg_text.strip(' ',1)
    if not args[0]:
        keyword = session.get('keyword', prompt='昨晚梦到了什么呢？')
    else:
        keyword = args[0]
    analyse = await get_dsp(keyword)
    await session.send(analyse, at_sender=True)
"""    
@dream.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['keyword'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的梦境不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
"""