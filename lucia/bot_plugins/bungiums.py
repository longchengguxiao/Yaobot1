
__plugin_name__='番剧更新'

headers = {'content-type': 'application/json'}
import aiohttp
import asyncio
import json
from nonebot.experimental.plugin import on_command
from nonebot.command import CommandSession
from datetime import datetime
import pytz
async def get_list():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as req:
            str_json = json.loads(await req.read())
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    list1 = []
    if str_json.get('message') == 'success':
        for result in str_json.get('result'):
            if result.get('date') =='{}-{}'.format(now.month,now.day):
                for item in result.get('seasons'):
                    bungium = {}
                    bungium['名称'] = item.get('title')
                    bungium['集数'] = item.get('pub_index')
                    bungium['时间'] = item.get('pub_time')
                    list1.append(bungium)
        return list1
    else:
        return '查询失败'

@on_command('bangumi',aliases=('番剧更新','番剧'))
async def _(session:CommandSession):
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    ans = await get_list()
    if ans == '查询失败':
        await session.send('查询失败', at_sender=True)
    else:
        str1 = '{}-{}-{}\n'.format(now.year,now.month,now.day)
        for bungium in ans:
            str1 += '《' + bungium['名称']+'》' + '于今日' + bungium['时间'] + '更新' + bungium['集数']+'\n'
        await session.send(str1)
