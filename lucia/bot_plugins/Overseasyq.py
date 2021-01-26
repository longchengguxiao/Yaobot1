# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 08:07:21 2021

@author: Lenovo
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio
import json
#with open(path,'w',encoding='utf-8') as f:
#    f.write(html.text)
#soup = BeautifulSoup(html,'lxml')

async def get_overseas_yq():

    #headers = {
    #    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    #    'referer':'https://news.qq.com/zt2020/page/feiyan.htm'
    #    }
    headers = {'content-type': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers = headers) as html:
            json1 = json.loads(await html.read())
    list1=[]
    i=1
    for item in json1.get('data'):
        overseas={}
        if (i == 1) or (i == 5) or (i== 8)  or (i == 4) or (i == 2) or (i == 6) or (i == 10) or (i == 22) :
            overseas['国家'] = item.get('name')
            overseas['新增确诊'] = item.get('confirmAdd')
            overseas['现有确诊'] = item.get('nowConfirm')
            overseas['确诊人数'] = item.get('confirm')
            overseas['死亡数'] = item.get('dead')
            overseas['治愈数'] = item.get('heal')
            list1.append(overseas)
        i += 1
        if i> 22:
            break
    return list1

@on_command('overseas', aliases=('海外情况','海外情况查询'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def overseas_yiqing(session: CommandSession):
    yq_report = await get_overseas_yq()
    str1 =''
    for item in yq_report :
        str1 += str(item)+'\n'
    await session.send(str1)
    
