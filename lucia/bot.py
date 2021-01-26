# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:38:14 2021

@author: Lenovo
"""

from os import path

import nonebot
import bot_config


nonebot.init(bot_config)
# 第一个参数为插件路径，第二个参数为插件前缀（模块的前缀）
nonebot.load_plugins(path.join(path.dirname(__file__), 'bot_plugins'), 'bot_plugins')

# 如果使用 asgi
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    nonebot.run()