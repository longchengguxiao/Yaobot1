# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:00:06 2021

@author: Lenovo
"""

from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg()
    except CQHttpError:
        pass
