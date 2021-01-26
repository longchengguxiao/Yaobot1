# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:24:00 2021

@author: Lenovo
"""
#所有模块已于2021-01-23 16:03全部实现
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
@on_command('功能', aliases=('功能查询', '你有什么功能'))
async def model(session: CommandSession):
    url = '已于2021-01-25更新完成\n登录页面获取详细信息'+'https://github.com/longchengguxiao/Yaobot1'
    await session.send(url)