# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 07:39:00 2021

@author: Lenovo
"""
from nonebot.command import CommandSession
from jieba import posseg
from nonebot.experimental.plugin import on_command
from nonebot.plugin import on_natural_language
from nonebot import  IntentCommand
from nonebot.natural_language import NLPSession
import http.client
import json
import urllib

import requests
from bs4 import BeautifulSoup


@on_command('weather', aliases=('天气', '天气预报', '查天气'))
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    weather_report = await get_weather(city)
    await session.send(weather_report, at_sender=True)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)
    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
            break
    return IntentCommand(80.0, 'weather', current_arg=city or '')


async def get_weather(city_name):
    city_code = get_city_code(city_name)
    weather_info = get_info(city_code)
    if weather_info:
        res = city_name + '的天气预报如下\n'
        for each in weather_info:
            res += '\n' + each[0] + ' ' + each[1] + ' '
            if each[2]:
                res += each[2] + '/'
            res += each[3]
        return res
    else:
        return '查询失败'


def get_info(city_code):
    try:
        url = 'http://www.weather.com.cn/weather/' + city_code + '.shtml'
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        div = soup.find('div', {'id': '7d'})
        li = div.find('ul').find_all('li')
        week_info = []
        for each in li:
            day_info = []
            day_info.append(each.find('h1').string)
            p = each.find_all('p')
            day_info.append(p[0].string)
            if p[1].find('span') is None:
                temp_high = None
            else:
                temp_high = p[1].find('span').string
            temp_low = p[1].find('i').string
            day_info.append(temp_high)
            day_info.append(temp_low)
            week_info.append(day_info)
        return week_info
    except:
        return None


def get_city_code(city_name):
    try:
        parameter = urllib.parse.urlencode({'cityname': city_name})
        conn = http.client.HTTPConnection('toy1.weather.com.cn', 80, timeout=5)
        conn.request('GET', '/search?' + parameter)
        r = conn.getresponse()
        data = r.read().decode()[1: -1]
        json_data = json.loads(data)
        code = json_data[0]['ref'].split('~')[0]
        return code
    except:
        return None