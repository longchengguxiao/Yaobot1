# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:24:13 2021

@author: Lenovo
"""
    
from baike import getBaike
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = '百度'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'

def get_baike(msg):
    ret = getBaike(msg,no=[1,[0]])
    return ret
@on_command('百度', aliases=('百度百科', '百度搜索', '搜索','度娘'),permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ', 1)
    if not args[0]:
        ret = session.get(key='ret', prompt='请问要搜索什么内容呢？(返回内容为百度百科)', at_sender=True)
    else :
        ret = args[0]
    ans = get_baike(ret)
    await session.send(ans,at_sender=True)