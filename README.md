# Yaobot1
基于nonebot的说明
'2021-01-23更新 v1.2.1\n现已开启功能：\n'
# '属性2.0
={keyword:attribute or 属性 or 今日属性 or 特性 or 我的特性, permission:群聊成员，支持自然语言解析}\n'
# '百科
={keyword:百度 or 百度百科 or 百度搜索 or 搜索 or 度娘, permission:群聊成员，支持自然语言解析}\n'（感谢github项目baike_api）
# '国内疫情查询2.0
={keyword:疫情 or 今日疫情 or 疫情查询 or 查疫情,permission:群聊成员，支持自然语言解析}\n'
# '开发日志 （为保障核心功能的正常运行，现已停止，如有需要请联系维护者）
={keyword:log or 更新日志,permission: 仅超级管理}\n' 
# '讲笑话
={keyword:joke or 讲个笑话吧 or 来一个笑话 or 笑话 or 说一个笑话,permission:任何聊天，支持自然语言解析}\n' 
# '音乐查询推送
={keyword:music or 点歌 or 音乐, permission:仅限群聊，支持自然语言解析}\n'
# '国外疫情查询 （为保障核心功能的正常运行，现已停止，如有需要请联系维护者）
={keyword:overseas or 海外情况 or 海外情况查询,permission: 仅限群聊}\n'
# 'setu2.0
={keyword:壁纸, permission: 仅超级管理, ps:谨慎使用，可能被风控}\n'
# 'ping
= {keyword:ping, permission: 仅超级管理, ps:测试bot的第一个样例}\n'
# '真心话题库
={keyword:真心话 or 真心话题目 or 来一个真心话题目 or 说一个真心话题目,permission:仅限群聊, ps:题库中仅有55道，欢迎补充}\n'
# '报时 （为保障核心功能的正常运行，现已停止，如有需要请联系维护者）
={keyword: none,permission:none,ps:自动整点报时，可添加群号}\n'
# '自定义对话
={keyword: variety, permission: 任何聊天, ps:可自定义，找我添加即可}\n'
# '天气查询2.0
={keyword:weather or 天气预报 or 天气查询 or 查天气,permission:任意聊天，支持自然语言解析, ps:输入城市如武汉即可，无需加市}\n'
# '迎新入群
={keyword:none,permission:none;ps:可添加群号}\n'
# '知乎日报
={keyword:zhihu or 知乎日报 ,permission:任何会话}\n'（感谢知乎提供的api）
# '历史上的今天2.0
={keyword：历史上的今天，peimission:仅限群聊，支持自然语言解析}\n'
# '网易云热评 （为保障核心功能的正常运行，现已停止，如有需要请联系维护者）
= {keyword：热评 or 网易云热评 or 网易云评论，permissin：仅限群聊}，支持自然语言解析\n
# '周公解梦
={keyword：周公解梦 or 梦的解析 or 解梦，permission：仅限群聊}\n'
# '微博热搜
={keyword：微博热搜 or微博 or 热搜 ，permission： 仅限群聊，支持自然语言解析}\n'
# '火星语翻译
={keyword：火星语 or 火星文 or  火星语转换 or 火星文转换，permission：仅限群聊}\n'
# '路径查看 （为保障核心功能的正常运行，现已停止，如有需要请联系维护者）
= {keyword: distance or 路径选择 or 路径查看 or 路径推送 permission: 任何会话}\n'（感谢百度地图提供的api）
# '番剧更新'
={keyword:bangumi or 番剧查询 or 番剧,perimission : 任何会话}\n
# 猜歌名
={keyword = 猜歌名 and 提示 ,permission : 仅群聊}\n
# 网抑云评论
={keyword = 网抑云 or 网抑，permission = 任意会话，支持自然语言解析}\n
# 禁言
={keyword = '暗影冲击'+空格+@+时间（分钟），permission：仅限群管理}
# 送礼物
={keyword = '给予王的馈赠' + @ + 礼物id（目前不可用）,permission:仅限群管理}
# 土味情话
={keyword = '你有什么想对我说的吗',permission:任意会话}
# 文字转语音
={keyword = ‘tts’or‘说句人话’，permission:仅群聊}
# 百度翻译
={keyword='翻译',permission:任意会话}\n(感谢百度翻译提供的api)
# 宠物系统
={keyword = '宠物系统',permission:仅群聊}宠物系统的详情请回复宠物系统来查看
# 鲁迅表情包
 = {keyword = '鲁迅说+空格+说的话',permission:仅群聊}
# 伪造聊天记录
 = {keyword = '伪造+空格+@+说的话'，permission：仅群聊 }
 # 我有一个朋友说
 ={keyword = '我有一个朋友说+空格+说的话',permission:仅群聊}
 # 发送群公告
 ={keyword：千里传音，permission：管理或超管}
 # 踢人
 ={keyword：流放 ，permission：管理或超管}
 # 撤回
 ={keyword = ‘回复消息+删除@+回溯’，permission：管理或超管}
 # 检查连接安全性
 ={keyword = “回复+删除@+占星术”，permission：管理或超管}
 # 石头剪刀布
 ={keyword=“石头”or“剪刀”or“布”，permission：任意群聊}、
 # 记账系统
 ={keyword :‘记账+空格+支出or收入+金额（+备注or理由）’，若无备注则默认填充一条备注，}
 ={keyword:‘余额查询’，在群里内可查询完整账单，且为保护隐私默认10秒撤回}
 ={keyword：‘上月账单查询’，同上}
# 留言系统
={keyword=‘留言+空格+留言内容（+空格+署名）’，若无署名则默认为QQ昵称}
# 单词系统
={keyword = '单词系统'}
# 大部分模块已于2021-02-05实现语言解析
# 全部模块已经于2021-02-05完善
# '所有模块已于2021-02-12 10：05全部实现'
# 已于2021-01-26 实现异步爬虫，更高效
