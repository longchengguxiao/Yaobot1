# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 23:18:56 2021

@author: Lenovo
"""
from nonebot.notice_request import NoticeSession
from nonebot.plugin import on_notice


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    
    # 发送欢迎消息
    await session.send('欢迎新同学呀！有啥事尽管问，我们尽力都回答',at_sender=True)
