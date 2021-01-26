# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 23:54:11 2021

@author: Lenovo
"""
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
#from nonebot import on_natural_language, NLPSession, IntentCommand
#from aiocqhttp import MessageSegment
#from jieba import posseg

__plugin_name__ = '对话'
__plugin_usage__ = '用法： 对我说 "对话"，我会回复 "回答"'

@on_command('smart', aliases=('谁最帅','sos团里谁最帅', '最帅的人是谁', 'sos团里最帅的人是谁', '谁是最帅的人', 'sos团里谁是最帅的人'))
async def smart(session: CommandSession):
    await session.send('最帅的人自然是团长啦！')


@on_command('foot', aliases=('谁最喜欢抠脚','最喜欢抠脚的人是谁', '谁经常抠脚'))
async def foot(session: CommandSession):
    await session.send('毫无疑问，自然是浩滨哥！')

@on_command('man', aliases=('每当这时，我便想起了那个为爱所困的男人', '每当这时，我便想起了那个为情所困的男人'))
async def man(session: CommandSession):
    await session.send('懂得都懂，我们说的是那位大人！')

@on_command('女装', aliases=('女装，只有一次和无数次'))
async def dress(session: CommandSession):
    await session.send('出轨也是')
    
@on_command('错过', aliases=('女人错过了那个她最想嫁的人 就会变得挑剔'))
async def miss(session: CommandSession):
    await session.send('男人错过那个他最想娶的人， 就会变的很随意。')
    
@on_command('forget', aliases=('我该如何忘了她'))
async def forget(session: CommandSession):
    await session.send('忘不了，就多想想')
    
@on_command('introduce', aliases=('介绍一下自己吧','出来介绍一下自己吧','给大家做个自我介绍吧'))
async def introduction(session: CommandSession):
    await session.send('大家好，我的名字叫小小垚，简称垚，英文名字叫lucia，欢迎大家和我一起交流一起学习哟。\n这是主人的邮箱1298919732@qq.com，如果我犯了什么错可千万不要告诉他（嘘~）\n如果想看我会什么本领可以对我说"功能"\n还请多多指教啦！')
 

"""
@on_natural_language(keywords=('谁最帅', '最帅的人', '谁是最帅的人'),only_to_me=False)
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    pic = None
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'st':
            pic = word.word
            break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90, 'setu', current_arg=pic)
"""