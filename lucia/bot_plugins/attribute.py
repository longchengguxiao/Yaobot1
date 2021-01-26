# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:08:08 2021

@author: Lenovo
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import random


__plugin_name__ = 'attribute'
__plugin_usage__ = '用法： 对我说 "attribute"，我会回复 "属性"'


@on_command('attribute',aliases=('属性', '今日属性', '特性','我的属性'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def _(session: CommandSession):
    fortune = random.randrange(59,100)
    Hp = random.randrange(59,100)
    wisedom = random.randrange(59,100)
    strength = random.randrange(59,100)
    smart = random.randrange(59,100)
    skill = random.randrange(59,100)
    miss = random.randrange(59,100)
    average = 1.0*fortune*0.2 + 1.0*Hp*0.1 + 1.0*wisedom*0.2 + 1.0*strength*0.15 + 1.0*smart*0.1 + 1.0*skill*0.15 + 1.0*miss*0.1
    shuxing = {
        "幸运值" : fortune,
        "智慧" : wisedom,
        "耐力" : Hp,
        "力量" : strength,
        "技术" : skill,
        "闪避" : miss,
        "颜值" : smart,
        "综合评分" : average
        }
    await session.send(str(shuxing), at_sender=True)