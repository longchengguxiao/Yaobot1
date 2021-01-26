# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:06:46 2021

@author: Lenovo
"""
#from jieba import posseg
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from datetime import datetime
import pytz
#from nonebot.plugin import on_natural_language
#from nonebot import  IntentCommand
#from nonebot.natural_language import NLPSession
import aiohttp
import asyncio
import json
async def get_yiqing():
    url = 'https://www.tianqiapi.com/api?version=epidemic&appid=23035354&appsecret=8YvlPNrz'
    #headers = {
     #   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
      #  }
    headers = {'content-type': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers = headers) as html:
            str_json = json.loads(await html.read())
    if str_json.get('errcode') == 0:
        pro = {}
        data = str_json.get('data')
    #    print(data[0]['cities'])
        for city in data.get('area'):
            name = city.get('provinceName')
            if name =='湖北':
                for item in city.get('cities'):
                    if item.get('city') =='武汉':
                        pro['武汉'] = {}
                        pro['武汉']['现有确诊'] =item.get('curConfirm') 
                        pro['武汉']['新增确诊'] = item.get('confirmAdd')
                        break
            elif name == '湖南':
                for item in city.get('cities'):
                    if item.get('city') == '衡阳':
                        pro['衡阳'] = {}
                        pro['衡阳']['现有确诊'] =item.get('curConfirm') 
                        pro['衡阳']['新增确诊'] = item.get('confirmAdd')
                        break
            elif name == '河南':
                for item in city.get('cities'):
                    if item.get('city') == '商丘':
                        pro['商丘'] = {}
                        pro['商丘']['现有确诊'] =item.get('curConfirm') 
                        pro['商丘']['新增确诊'] = item.get('confirmAdd')
                        break
            elif name == '内蒙古':
                for item in city.get('cities'):
                    if item.get('city') == '鄂尔多斯':
                        pro['鄂尔多斯'] = {}
                        pro['鄂尔多斯']['现有确诊'] =item.get('curConfirm') 
                        pro['鄂尔多斯']['新增确诊'] = item.get('confirmAdd')
                        break
            elif name == '吉林':
                for item in city.get('cities'):
                    if item.get('city') == '松原':
                        pro['松原'] = {}
                        pro['松原']['现有确诊'] =item.get('curConfirm') 
                        pro['松原']['新增确诊'] = item.get('confirmAdd')
                        break
            elif name == '陕西':
                for item in city.get('cities'):
                    if item.get('city') == '西安':
                        pro['西安'] = {}
                        pro['西安']['现有确诊'] =item.get('curConfirm') 
                        pro['西安']['新增确诊'] = item.get('confirmAdd')
                        break
        return pro
    else:
        return '查询失败'


@on_command('yiqing', aliases=('疫情', '今日疫情', '查疫情','疫情查询'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def yiqing(session: CommandSession):
    #args = session.current_arg_text.strip(' ',1)
    #if not args[0]:  
    #city = session.get('city', prompt='你想查询哪个城市的疫情呢？(xx省)')
    #else:
    #    city = args[0]
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    yq_report = await get_yiqing()
    str1 = ''
    str1 +=str(now.year)+'-'+ str(now.month) + '-' + str(now.day)+'\n' + '武汉现有确诊：' + str(yq_report['武汉']['现有确诊']) +' 新增确诊' + str(yq_report['武汉']['新增确诊']) + '\n'
    str1 += '商丘现有确诊：' + str(yq_report['商丘']['现有确诊']) +' 新增确诊' + str(yq_report['商丘']['新增确诊'])+'\n'
    str1 += '衡阳现有确诊：' + str(yq_report['衡阳']['现有确诊']) +' 新增确诊' + str(yq_report['衡阳']['新增确诊'])+'\n'
    str1 += '松原现有确诊：' + str(yq_report['松原']['现有确诊']) +' 新增确诊' + str(yq_report['松原']['新增确诊'])+'\n'
    str1 += '鄂尔多斯现有确诊：' + str(yq_report['鄂尔多斯']['现有确诊']) +' 新增确诊' + str(yq_report['鄂尔多斯']['新增确诊'])+'\n'
    await session.send(str1)
    
"""
@yiqing.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
    
@on_natural_language(keywords={'疫情'}, only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)
    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
            break
    return IntentCommand(80.0, 'yiqing', current_arg=city or '')
"""