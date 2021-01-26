

__plugin_name__ = '地理信息推送'

from services import  baidu
from nonebot.experimental.plugin import on_command
from nonebot.command import CommandSession
from nonebot.message import MessageSegment
import requests
AK = baidu.BAIDU_AK()

URL = 'http://api.map.baidu.com/place/v2/search?query={}&region={}&output=json&ak={}'

def get_location(keyword,city):
    req = requests.get(URL.format(keyword,city,AK))
    str_json = req.json()
    if str_json.get('message') == 'ok':
        data = str_json.get('results')[0]         
        return data.get('location')
    else :
        return '查询失败'

@on_command('位置',aliases=('位置查询','位置推送','位置获取'))
async def _(session:CommandSession):
    city = session.get('city', prompt='输入您所在城市')
    keyword = session.get('keyword', prompt='输入您要查询的具体位置')
    location = get_location(keyword, city)
    reps = MessageSegment.location(location['lat'], location['lng'])
    await session.send(reps)
    
