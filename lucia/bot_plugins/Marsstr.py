
__plugin_name__ = '火星语转换'
#headers = {
#    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
#    }
headers = {'content-type': 'application/json'}
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import aiohttp
import asyncio
import json

async def get_Mars(keyword):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(keyword,Appkey), headers = headers) as req:
            str_json = json.loads(await req.read())
    if str_json.get('reason') == 'Return Successd!':
        return str_json.get('outstr')
    else:
        return '很抱歉转换失败'

@on_command('火星语',aliases=('火星文', '火星语转换', '火星文转换'), permission=lambda sender: (not sender.is_privatechat) or sender.is_superuser)
async def Mars(session:CommandSession):
    #args = session.current_arg_text.strip(' ',1)
    #if not args[0]:
    keyword = session.get('keyword', prompt='你想翻译什么内容呢？')
    #else:
    #    keyword = args[0]
    Marsstr = await get_Mars(keyword)
    await session.send(Marsstr, at_sender=True)

@Mars.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['keyword'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要翻译的内容不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg
