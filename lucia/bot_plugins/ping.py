# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:40:00 2021

@author: Lenovo
"""

"""
一个插件最好能够定义其插件名和介绍，正如 __plugin_name__ 和 __plugin_usage__ 一样。

on_command 装饰器会将一个函数注册为命令处理器，其中第一个参数为命令的名字，在这里我还设置了此命令的权限：lambda sender: sender.is_superuser 表示只有超级用户（也就是你）才能够触发这条命令，机器人会无视其余用户。

当命令被触发时，nonebot 会创建一个 CommandSession 对象用来代表当前的会话。在这里我们向发送者发送回一条信息。

这就是最小的 nonebot 机器人实例，你现在可以使用 python bot.py 命令来运行此程序，不过仅靠这还不行，因为我们现在还没有后端
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command


__plugin_name__ = 'ping'
__plugin_usage__ = '用法： 对我说 "ping"，我会回复 "pong!"'


@on_command('ping', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    await session.send('pong!')