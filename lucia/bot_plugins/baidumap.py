# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:35:18 2021

@author: Lenovo
"""

__plugin_name__ = '地理信息推送'

import aiohttp
import asyncio
import json
from services import  baidu
from nonebot.experimental.plugin import on_command
from nonebot.command import CommandSession
AK = baidu.BAIDU_AK()

#获取经纬坐标
URL1 = 'http://api.map.baidu.com/place/v2/search?query={}&region={}&output=json&ak={}'
#获取公交信息
URL2 = 'http://api.map.baidu.com/direction/v2/transit?origin={},{}&destination={},{}&ak={}'
#获取骑行信息
URL3 = 'http://api.map.baidu.com/direction/v2/riding?origin={},{}&destination={},{}&ak={}'
#获取驾车信息
URL4 = 'http://api.map.baidu.com/direction/v2/driving?origin={},{}&destination={},{}&ak={}'

#headers = {
#    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }
headers = {'content-type': 'application/json'}

async def get_location(keyword,city):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL1.format(keyword,city,AK),headers = headers) as req:
            str_json = json.loads(await req.read())
    str_json = req.json()
    if str_json.get('message') == 'ok':
        data = str_json.get('results')[0]         
        return data.get('location')
    else :
        return '查询失败'
async def get_distance_dirving(url,location1,location2):
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(location1['lat'],location1['lng'],location2['lat'],location2['lng'],AK)) as req2:
            str2_json = json.loads(await req2.read())
    if str2_json.get('status') == 0:
        data = str2_json.get('result')
        routes = data.get('routes')
        list1 = []
        for route in routes:
            sec={}
            sec['路程'] = route.get('distance')
            sec['时间'] = route.get('duration')
            #sec['出租车费用'] = route.get('taxi_fee')
            list1.append(sec)
    return list1
async def get_distance_bus(url,location1,location2):
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(location1['lat'],location1['lng'],location2['lat'],location2['lng'],AK)) as req2:
            str2_json = json.loads(await req2.read())
    if str2_json.get('status') == 0:
        data = str2_json.get('result')
        routes = data.get('routes')
        list1 = []
        for route in routes:
            sec={}
            sec['路程'] = route.get('distance')
            sec['时间'] = route.get('duration')
            #sec['到达时间'] = route.get('arrive_time')
            list1.append(sec)
    return list1
async def get_distance_riding(url,location1,location2):
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(location1['lat'],location1['lng'],location2['lat'],location2['lng'],AK)) as req2:
            str2_json = json.loads(await req2.read())
    if str2_json.get('status') == 0:
        data = str2_json.get('result')
        routes = data.get('routes')
        list1 = []
        for route in routes:
            sec={}
            sec['路程'] = route.get('distance')
            sec['时间'] = route.get('duration')
            list1.append(sec)
    return list1            
        
    
@on_command('distance', aliases=('路径选择','路径查看','路径推送','路经查询','路径'))
async def dis(session:CommandSession):
    str3 = ''
    city = session.get('city',prompt='请输入您所在城市')
    keyword1 = session.get('keyword1',prompt='请输入起点位置')
    keyword2 = session.get('keyword2',prompt='请输入终点位置')
    location1 = await get_location(keyword1,city)
    location2 = await get_location(keyword2,city)
    if (keyword1 != '查询失败') and (keyword2 != '查询失败'):
        #way = session.get('way',prompt='请输入您出行的方式，公交请输入1，骑行请输入2,驾车(或出租)请输入3')
        #if way == '1':
        ans1 = await get_distance_bus(URL2, location1, location2)
        #elif way =='2':
        ans2 = await get_distance_riding(URL3, location1, location2)
        #elif way == '3':
        ans3 = await get_distance_dirving(URL4, location1, location2)
            
        str3 += '公交路程:'+str(float(ans1[0]['路程'])/1000)+'km\n'+'时间:'+str(float(ans1[0]['时间'])/60) + 'min\n'
        str3 += '骑行路程:'+str(float(ans2[0]['路程'])/1000)+'km\n'+'时间:'+str(float(ans2[0]['时间'])/60) + 'min\n'
        str3 += '驾车路程:'+str(float(ans3[0]['路程'])/1000)+'km\n'+'时间:'+str(float(ans3[0]['时间'])/60) +'min'
        await session.send(str3, at_sender=True)
    else:
        await session.send('获取位置信息失败', at_sender=True)
    