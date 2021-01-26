# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:41:54 2021

@author: Lenovo
"""

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import random

__plugin_name__ = '真心话'
__plugin_usage__ = '用法： 对我说 "真心话"，我会回复 "回答"'


@on_command('真心话', aliases=('说一个真心话题目', '来一个真心话题目','真心话题目'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser )
async def _(session: CommandSession):
    num = random.randrange(0,55)
    list_1 = []
    path = r'D:\luciabot\useless\真心话.txt'
    with open(path,'r',encoding='utf-8') as f:
        list_1 = f.readlines()    
    await session.send(list_1[num])