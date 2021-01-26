# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:39:05 2021

@author: Lenovo
"""

from nonebot.default_config import *

from datetime import timedelta

# 我们不使用命令前缀
COMMAND_START = { '' }

SESSION_CANCEL_EXPRESSION = (
    '好的',
    '好的吧',
    '好吧，那lucia就不打扰啦',
    '那lucia先不打扰大家啦',
)
# 机器人昵称，设定后 "@机器人 天气" 和 "lucia 天气" 效果相同。
NICKNAME = { 'lucia', '垚', '小小垚' }
# 关闭调试输出，提升性能。
DEBUG = False
# 表示“超级用户”，也就是机器人的主人。超级用户拥有最高的权限。在这里填入你的 QQ 号。
SUPERUSERS = { 1298919732 , 279764456}
# 表示一条命令的超时（没有用户输入）时间。
SESSION_RUN_TIMEOUT = timedelta(seconds=10)
# 服务器和端口
HOST = '127.0.0.1'
PORT = 8765

API_ROOT = 'http://127.0.0.1:8765'

SHORT_MESSAGE_MAX_LENGTH = 2000

