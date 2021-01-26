# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:32:03 2021

@author: Lenovo
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

__plugin_name__ = '更新日志'

@on_command('log', aliases=('更新日志'),permission=lambda sender: sender.is_superuser)
async def upgrade(session: CommandSession):
    part1 = '2021-01-20 v1.0.0: 学习document1并正式启用机器人，插件添加：天气查询1.0；属性；ping\n'
    part2 = '2021-01-21 v1.0.1: 学习document2，添加报时功能并根据反映添加自定义对话,联系之前项目添加joke模块链接微软小冰,但学习图片发送失败setu1.0告终\n'
    part3 = '2021-01-22 v1.1.0: 学习document3搭建docker失败。查看文档学习更加底层的知识，成功发送图片并实现setu2.0\n'
    part4 = '2021-01-23 v1.1.1: 理解了api接口的重要性，查取一些api地址后搭建了疫情查询以及知乎。源于github的文件添加模块百科\n'
    development_log = part1+part2+part3+part4
    await session.send(development_log())