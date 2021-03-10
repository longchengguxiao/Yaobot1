# [Yaobot](https://github.com/longchengguxiao/Yaobot1)

## 目录

+ 2021-3-10更新文档

+ 基于**[Nonebot](#Nonebot)** + **[Go-CQHttp](#Go-CQHttp)**打造的QQ**功能型**机器人。
+ 生态
  + [x] [单词系统2.0](#单词系统)——学习使我快乐
  + [ ] [校园系统](#校园系统)——XDer专属(有待补全)
  + [x] [留言系统](#留言系统)——用的人少得可怜，不过会多的，对吧？
  + [x] [账单系统](#账单系统)——只有本人在使用的系统
  + [x] [查询系统](#查询系统)——方便你我他
  + [x] [娱乐系统](#娱乐系统)——群内活跃气氛小助手
  + [x] [你懂的系统](#你懂的)——不要一上来就点开这个啊喂！！！
  + [x] [恶意系统](#恶意系统)——最不想开启但却又很好奇
  + [ ] [宠物系统](#宠物系统)——测试中！
  + [x] [群聊系统](#群聊系统)——看起来十分有用的样子呢
  + [ ] [人工智能系统](#人工智能)——有待开发
  + [x] [超级管理](#超级管理)——便于维护bot
    + [x] [黑名单](#黑名单)
    + [x] [模块管理2.0](#模块管理)
    + [x] [bug提交反馈](#bug反馈)
  + [x] [被大家嫌弃的功能](#小黑屋)——被拖入小黑屋的功能

+ [术语注释](#术语注释)
+ [特别感谢](#特别感谢)

------

## 生态

### 单词系统

​	作为第一个**学习**插件，自然是要写在最前面。

##### 背单词：

| [关键字/格式](#关键字/格式) | [权限](#权限) |              [描述](#描述)               | [备注](#备注) |
| :-------------------------: | ------------- | :--------------------------------------: | ------------- |
| “word”/“背单词”/“单词打卡”  | 任何人        | 返回一个单词，若在群聊则额外返回一个语音 | 无CD          |

##### 单词查询:

|     [关键字/格式](#关键字/格式)     | [权限](#权限) |  [描述](#描述)   | [备注](#备注) |
| :---------------------------------: | ------------- | :--------------: | ------------- |
| "词典"/"单词查询"+空格+要查询的单词 | 任何人        | 返回该单词的意思 | 无CD          |

##### 单词添加及移除:

|        [关键字/格式](#关键字/格式)        |                        [权限](#权限)                         |   [描述](#描述)    | [备注](#备注) |
| :---------------------------------------: | :----------------------------------------------------------: | :----------------: | :-----------: |
| “单词写入”+空格+单词/“单词移除”+空格+单词 | 单词写入为任何人，单词添加为仅超级管理（因为截止到目前为止只有少部分人在用，所以并没有为个性化即用户制定单词计划的倾向） | 添加或移除一个单词 |     无CD      |

##### 打卡计划查询:

| [关键字/格式](#关键字/格式) | [权限](#权限) |            [描述](#描述)             | [备注](#备注) |
| :-------------------------: | :-----------: | :----------------------------------: | :-----------: |
|    “打卡任务”/“单次任务”    |  仅超级管理   | 返回今天的打卡目标以及已完成单词数量 |     无CD      |

##### 单词重置：

| [关键字/格式](#关键字/格式) | [权限](#权限) |     [描述](#描述)      | [备注](#备注) |
| :-------------------------: | :-----------: | :--------------------: | :-----------: |
|         “单词重置”          |  仅超级管理   | 重置今天的单词打卡任务 |     无CD      |

##### 定时单词任务提醒：

| [关键字/格式](#关键字/格式) |    [权限](#权限)     |        [描述](#描述)         |      [备注](#备注)       |
| :-------------------------: | :------------------: | :--------------------------: | :----------------------: |
|             无              | 仅超级管理（可定制） | 向目标用户推送今天的打卡情况 | 无CD，可向维护者申请权限 |

##### 单词系统关键字：

| [关键字/格式](#关键字/格式) | [权限](#权限) | [描述](#描述)                | [备注](#备注) |
| :-------------------------: | ------------- | ---------------------------- | ------------- |
|         “单词系统”          | 任何人        | 返回该系统内拥有权限的关键词 | 无CD          |

--------

### 校园系统

​	部分移植于电表，源于在电表查询流量余额失败便想移植至bot从而更方便查询。（特此说明，账号在内部储存形式为md5加密后，且可以随时解绑，安全问题可以放心）

##### 账号绑定及解绑

##### 图书查询

##### 流量查询

##### 成绩查询

|   [关键字/格式](#关键字/格式)    |          [权限](#权限)           |                        [描述](#描述)                         | [备注](#备注) |
| :------------------------------: | :------------------------------: | :----------------------------------------------------------: | :-----------: |
|            "账号绑定"            |        仅私聊(为保护隐私)        |                      将校园账号与QQ绑定                      |     无CD      |
| "账号解绑"/"解绑"/"账号解除绑定" |             任意会话             |                    解除校园账号与QQ的绑定                    |     无CD      |
|        "图书查询"/"查书"         |              仅群聊              | 交互式对话，根据指令进行，最后返回图书信息(相较于公众号更详细) |     无CD      |
|     "图书推荐"/"图书排行榜"      |              仅群聊              |       返回一个合并回话，内容为新书速递与图书借阅排行榜       |     无CD      |
|   "流量查询"/"校园网流量查询"    |       仅群聊(且需绑定账号)       |       返回您当前在线设备ip以及当前已使用流量及剩余流量       |     无CD      |
|       "成绩查询"/"查成绩"        | 任意会话(为保护隐私)且需绑定账号 |                    返回您最近一学期的成绩                    |  CD为300sec   |

--------

### 留言系统

​	相较于QQ消息，他的优点是可以告诉你对方是否查看信息，并在对方查看信息时通知你。（由于目前使用人数较少，所以仅限向我留言，后续有计划开放权限）

##### 留言：

|                 [关键字/格式](#关键字/格式)                  | [权限](#权限)  |           [描述](#描述)           | [备注](#备注) |
| :----------------------------------------------------------: | -------------- | :-------------------------------: | ------------- |
| “留言/留言板/树洞”+空格+留言信息（+空格+署名）（如果没有署名默认为QQ昵称） | 仅限私聊小小垚 | 传输到服务器中一条被md5加密的信息 | 无CD          |

##### 查阅：

| [关键字/格式](#关键字/格式) | [权限](#权限) |                     [描述](#描述)                      | [备注](#备注) |
| :-------------------------: | ------------- | :----------------------------------------------------: | ------------- |
|           “查阅”            | 仅超级管理    | 返回一条待查阅的消息，同时提醒消息发送者消息已经被查阅 | 无CD          |

##### 定时汇报：

| [关键字/格式](#关键字/格式) | [权限](#权限) |          [描述](#描述)           | [备注](#备注) |
| :-------------------------: | ------------- | :------------------------------: | ------------- |
|             无              | 仅超级管理者  | 发送一条带有未查阅信息数量的消息 | 无CD          |

##### 留言系统关键字：

| [关键字/格式](#关键字/格式) | [权限](#权限) |        [描述](#描述)         | [备注](#备注) |
| :-------------------------: | ------------- | :--------------------------: | ------------- |
|          留言系统           | 任何人        | 返回该系统内拥有权限的关键词 | 无CD          |

---------

## 账单系统

相较于其他记账app来说，该系统的优点是...更方便？（x）

虽然此系统目前只服务于我个人，但我相信他一定会越来越好的！！！会吗？

##### 记账：

|         [关键字/格式](#关键字/格式)         | [权限](#权限) |      [描述](#描述)       | [备注](#备注) |
| :-----------------------------------------: | ------------- | :----------------------: | ------------- |
| “记账”+空格+‘’支出/收入“+金额（支持浮点数） | 仅私聊        | 向服务器发送一条账单记录 | 无CD          |

##### 余额查询：

| [关键字/格式](#关键字/格式) | [权限](#权限) |                        [描述](#描述)                         | [备注](#备注) |
| :-------------------------: | :-----------: | :----------------------------------------------------------: | :-----------: |
|     “余额查询/查询余额”     |    任何人     | 返回账单总计若是群聊则额外返回一条详细账单信息并且在10秒后自动撤回 |     无CD      |

##### 上月账单查询：

| [关键字/格式](#关键字/格式) | [权限](#权限) | [描述](#描述) | [备注](#备注) |
| :-------------------------: | :-----------: | :-----------: | :-----------: |
|       “上月账单查询”        |    任何人     | 返回信息同上  |     无CD      |

##### 账单系统关键字：

| [关键字/格式](#关键字/格式) | [权限](#权限) |       [描述](#描述)        | [备注](#备注) |
| :-------------------------: | :-----------: | :------------------------: | :-----------: |
|         “账单系统”          |    任何人     | 返回该系统内有权限的关键字 |     无CD      |

>  下面为个人服务，[无需要可以直接跳转至下一章](#查询系统)

##### 家庭基金存入与支出

##### 家庭基金查询

##### 家庭基金系统

|       [关键字/格式](#关键字/格式)        | [权限](#权限) |      [描述](#描述)       | [备注](#备注) |
| :--------------------------------------: | :-----------: | :----------------------: | :-----------: |
| “家庭基金存入”/“家庭基金指出”+空格+ 金额 |  仅超级管理   | 向服务器发送一条账单消息 |     无CD      |
|              "家庭基金账单"              |  仅超级管理   |       返回详细账单       |     无CD      |
|               家庭基金系统               |  仅超级管理   |       返回系统指令       |     无CD      |

--------

### 查询系统

​	其中拥有着本bot第一个开发的插件——疫情查询！（可惜失效了，不过本维护者会尽力把这个坑填上的）本系统属于功能性系统，是一些功能性服务，如有其他需要可以联系维护者。

##### [梦的解析](#梦的解析)

##### [百度百科](#百度百科)（感谢[baike_api](https://github.com/1MLightyears/baike)）

##### [番剧查询](#番剧查询)

##### [火星语翻译](#火星语)

##### [链接安全查询](#链接安全查询)

##### [歌曲查询](#歌曲查询)

##### [历史上的今天](#历史上的今天)

##### [词云](#词云)

##### [翻译](#翻译)(感谢百度翻译平台)

##### [天气查询](#天气查询)

##### [微博热搜](#微博热搜)

##### [功能查询](#功能查询)

##### [缩写查询](#缩写查询)

##### [今日新闻](#今日新闻)

|              [关键字/格式](#关键字/格式)               |    [权限](#权限)     |                    [描述](#描述)                     | [备注](#备注) |
| :----------------------------------------------------: | :------------------: | :--------------------------------------------------: | :-----------: |
|       <a href="#梦的解析">“梦的解析”/“解梦”</a>        |  仅群聊(黑名单除外)  |               交互式对话，返回梦境解析               |     无CD      |
|       <a href="#百度百科">“百度”/“百度搜索”</a>        |  仅群聊(黑名单除外)  |             交互式对话，返回百度百科词条             |   CD为30sec   |
|       <a href="#番剧查询">"番剧"/“番剧更新”</a>        |        所有人        |                 返回今日番剧更新列表                 |     无CD      |
|        <a href="#火星语">“火星语”/“火星文”</a>         |        仅群聊        |            交互式对话，返回翻译好的火星文            |     无CD      |
| <a href="#链接安全查询">回复该链接并除去@后+占星术</a> |        仅群聊        |        返回该链接是否安全（安全，危险，未知）        |     无CD      |
|             <a href="#歌曲查询">“点歌”</a>             |   仅群聊(除黑名单)   | 交互式对话，返回歌曲卡片（QQ音乐），暂不支持查询歌手 |   CD为20sec   |
|       <a href="#历史上的今天">“历史上的今天”</a>       |        仅群聊        |       返回一个合并转发文本，内容为历史上的今天       |     无CD      |
|  <a href="#词云">“我的词云”/”本群词云“/”词云总览“</a>  | 分情况（黑名单除外） |         生成词云，根据命令不同生成不同的词云         |   CD为15sec   |
|               <a href="#翻译">“翻译”</a>               |        任何人        |           交互式对话，返回一条翻译后的文本           |     无CD      |
|       <a href="#天气查询">“天气”/“天气预报”</a>        |        任何人        |           交互式对话，返回要查询地点的天气           |     无CD      |
|           <a href="#微博热搜">“微博热搜”</a>           |        仅群聊        |       返回一条微博热搜，成为人们茶余饭后的谈资       |     无CD      |
|       <a href="#功能查询">“功能”/“功能查询”</a>        |        任何人        |                      查看本文档                      |     无CD      |
|    <a herf="缩写查询">“缩写/缩写查询”+空格+缩写</a>    |        仅群聊        |                   返回一条缩写释义                   |     无CD      |
|      <a href="今日新闻">"今日新闻"/"今日大事"</a>      |        仅群聊        |      返回一个合并转发文本，内容为今日或昨日大事      |     无CD      |
|                                                        |                      |                                                      |               |

------

### 娱乐系统

啊~终于到娱乐系统了，最精彩的部分要来啦！本系统属于娱乐性系统，是一些娱乐性服务，如有其他需要可以联系维护者。

##### 网抑云评论

##### 今日属性(签到)

##### 猜歌名

##### 土味情话

##### 戳一戳

##### 鲁迅说

##### 伪装

##### 我有一个朋友说（经典老梗）

##### 真心话

##### 猜灯谜

##### 文字转语音

##### 知乎日报


|  [关键字/格式](#关键字/格式)   |    [权限](#权限)     |                        [描述](#描述)                         | [备注](#备注) |
| :----------------------------: | :------------------: | :----------------------------------------------------------: | :-----------: |
|        “网抑云“/”网抑“         |  仅群聊(黑名单除外)  |                       返回一条催泪热评                       |   CD为10sec   |
|       ”属性“/”今日属性“        |        仅群聊        |          返回一条你的专属属性，再次询问可以获得排名          |     无CD      |
|            ”猜歌名“            | 仅群聊（黑名单除外） |        第一次返回一条前奏语音，第二次返回一条副歌语音        |     无CD      |
|       “你想对我说些什么”       |        任何人        | 返回一条土味情话（若为“爱你在心口难开则为bug请尽快[汇报](#超级管理)”） |     无CD      |
|    双击小小垚头像(即戳一戳)    |  仅群聊(黑名单除外)  |         返回一条消息，注意不要短时间内连续戳小小垚哟         |   CD为45sec   |
|    “鲁迅说”+空格+你想说的话    |   任何人(除黑名单)   |                         返回一张图片                         |   CD为10sec   |
|     “伪装”+空格+@+要说的话     | 仅群聊（黑名单除外） |            返回一个合并转发文本，内容为伪装后对话            |   CD为10sec   |
| “我有一个朋友说”+空格+要说的话 | 仅群聊（黑名单除外） |          返回一个合并转发文本，内容为我有一个朋友说          |   CD为10sec   |
|            “真心话”            |        仅群聊        | 返回一条真心话题目（题库中目前仅55条，如有需要请自行寻找并联系维护者添加） |     无CD      |
|            “猜灯谜”            |        仅群聊        |                 先返回题目，20sec后返回结果                  |     无CD      |
|        ”tts“/”说句人话“        |        仅群聊        |                   交互式对话，返回一条语音                   |     无CD      |
|           ”知乎日报“           |        任何人        |                      返回当日的知乎日报                      |     无CD      |

-------

### 你懂的系统

​	你不要过来啊！不要过来啊！我容易坏掉的！

##### 壁纸

##### Pixiv

| [关键字/格式](#关键字/格式) |    [权限](#权限)     |                        [描述](#描述)                         |                [备注](#备注)                |
| :-------------------------: | :------------------: | :----------------------------------------------------------: | :-----------------------------------------: |
|           “壁纸”            | 仅群聊（黑名单除外） |                   返回一条精美的二次元壁纸                   |                  CD为30sec                  |
|           “setu”            | 仅群聊（黑名单除外） | 返回一个“小孩子可以看的”pixiv图片（已修改像素）才不是什么磨砂卡贴呢！！！ | CD为20sec，如果有发现大量获取立即拉入黑名单 |
|      "pix"+空格+车牌号      |        仅私聊        |                     返回原图，请注意身体                     |  CD为15sec，如果发现大量获取立即拉入黑名单  |

------

### 恶意系统

​	可恶啊！听名字就知道不是什么好东西了！哼哼！！！

##### 防撤回

##### 防闪照

均为自动触发，但是可以禁用，消息二次撤回即可（如果你有权限的话），闪照直接撤回即可

------

### 宠物系统

再次鸣谢我的同学兼好舍友，SOS团的团长——李某人，为宠物文案做出巨大且不可磨灭的贡献

##### 获得蛋

##### 孵化

##### 喂食

##### 抚摸

##### 决斗

##### 宠物系统

##### 宠物档案

| [关键字/格式](#关键字/格式) |    [权限](#权限)     |                        [描述](#描述)                         | [备注](#备注) |
| :-------------------------: | :------------------: | :----------------------------------------------------------: | :-----------: |
|         “抽奖”/“蛋”         | 仅群聊（黑名单除外） | 抽取一枚宠物蛋，只可抽取一次，且宠物与你绑定，如要修改请练习维护者 |     无CD      |
|           “孵化”            | 仅群聊（黑名单除外） |                    返回宠物名称，孵化成功                    |     无CD      |
|      “投食”以及“抚摸”       | 仅群聊（黑名单除外） | 返回好感度上升情况（好感度暂未完善，如有好的想法可以联系维护者） |     无CD      |
|   “决斗”+空格+@宠物拥有者   | 仅群聊（黑名单除外） |          返回一个合并转发的消息，内容为宠物战斗过程          |   CD为15sec   |
|          宠物系统           |        仅群聊        |                     返回该系统内的关键词                     |     无CD      |
|         “搭档档案”          |        仅群聊        |                 返回你所拥有的宠物的详细信息                 |     无CD      |

--------

### 群聊系统

依据现有群聊功能实现（有些需要bot获得管理员权限）

##### 禁言（需要管理员权限）

##### 送礼物

##### 群聊踢人（需要管理员权限）

##### 发送群公告（需要管理员权限）

##### 宣布龙王

##### 欢迎新人

##### 通告群成员退群

##### 通告有人想要添加群聊

##### 通告运气王

| [关键字/格式](#关键字/格式) |   [权限](#权限)    |       [描述](#描述)        | [备注](#备注) |
| :-------------------------: | :----------------: | :------------------------: | :-----------: |
|    “变羊术”+空格+@+时间     | 仅群管理或超级管理 |          禁言某人          |     无CD      |
|    ”给予王的馈赠“+空格+@    |     仅超级管理     |        给某人送礼物        |     无CD      |
|        “流放”+空格+@        | 仅群管理或超级管理 |          踢出某人          |     无CD      |
|  “千里传音”+空格+想说的话   | 仅群管理或超级管理 |         发送群公告         |     无CD      |
|             无              |         无         |        宣布今日龙王        |     无CD      |
|             无              |         无         | 欢迎新人（可以订制欢迎词） |     无CD      |
|             无              |         无         | 通告有群成员退群（可订制） |     无CD      |
|             无              |         无         |     通知管理员有人加群     |     无CD      |
|             无              |         无         |         通告运气王         |     无CD      |

--------

### 人工智能系统

唔，一个伪装的人工智能，还在开发中

##### RPS

##### 自定义对话（别骂了在学了在学了）

|                 [关键字/格式](#关键字/格式)                  | [权限](#权限) |                      [描述](#描述)                       | [备注](#备注) |
| :----------------------------------------------------------: | :-----------: | :------------------------------------------------------: | :-----------: |
| “石头”/“剪刀”/“布”，但如果你想查看规则那么请回复“石头剪刀布” |    任何人     | 返回结果（帮忙收集一下训练数据吧求求了，多和他玩一会吧） |     无CD      |
|                      “自定义对话关键字”                      |    任何人     |                    返回自定义对话内容                    |     无CD      |

--------

### 超级管理

##### 黑名单

>|     [关键字/格式](#关键字/格式)     |  [权限](#权限)   |  [描述](#描述)   | [备注](#备注) |
>| :---------------------------------: | :--------------: | :--------------: | :-----------: |
>|    "黑名单"/“暗杀”/“拉黑”+空格+@    |    仅超级管理    | 把某人拉入黑名单 |     无CD      |
>| “取消拉黑”/“拉白”/“解除暗杀”+空格+@ |    仅超级管理    | 把某人拉除黑名单 |     无CD      |
>|    “暗杀名单列表”/“查看暗杀名单”    | 仅超级管理且群聊 |  查看黑名单列表  |     无CD      |

##### 模块管理

>| [关键字/格式](#关键字/格式) |     [权限](#权限)      |                   [描述](#描述)                    | [备注](#备注) |
>| :-------------------------: | :--------------------: | :------------------------------------------------: | :-----------: |
>|       “功能使用情况”        | 仅去聊（且黑名单除外） |     返回一个合并转发会话，内容为各功能使用情况     |     无CD      |
>|        “启用”/“禁用”        |       仅超级管理       | 启用或禁用某个模块（先使用功能状态查看名字后禁用） |     无CD      |
>|         “功能状态”          |    仅超级管理且群聊    |                  查看功能使用状态                  |     无CD      |

##### bug反馈

>|   [关键字/格式](#关键字/格式)   | [权限](#权限) |                        [描述](#描述)                         | [备注](#备注) |
>| :-----------------------------: | :-----------: | :----------------------------------------------------------: | :-----------: |
>| “反馈”/“问题反馈”+空格+反馈内容 |    任何人     | 反馈给我一条bug（注意写清楚出现问题的功能以及出现问题的方式） |     无CD      |

--------

### 小黑屋

​	呜呜呜！我要哭死在这里！谁也别拦着我！

​	***请注意！以下功能均已被禁用！*** 

##### 报时功能

+ 因为过于***鸡肋***而被除去

##### 位置卡片

+ [Go-CQHttp](#Go-CQHttp)暂***未完善***该功能

##### 网易云热评

+ 太多***饭圈言论***而被禁用

##### 路经查询

+ 功能为实现两点之间**路径计算**（距离，时间），但苦于**没人使用**后除去

##### 海外疫情查询

+ 唔，貌似没人关心的样子呢

##### 头衔修改

+ **权限太高**从而去除

------

## 术语注释

#### Nonebot

+ 一个优秀的开源的框架，访问其项目地址[请点击这里](https://github.com/nonebot/nonebot)

#### Go-CQHttp

+ 一个优秀的开源服务器，访问其项目地址[请点击这里](https://github.com/Mrs4s/go-cqhttp)

#### 关键字/格式

+ 有些为精确关键字，有些为模糊关键字（在句子中掺杂着也会被认出，但必须保证完整），***建议使用精确关键字***
+ 请注意命令的格式，格式错误将不被触发

#### 权限

+ 需要**至少**为这个权限才可以使用该功能

#### 描述

+ 对于该功能的状态描述

#### 备注

+ 对于CD等事项的注释

点此返回[目录](#目录)

------

## 特别感谢

> 此项为特别感谢名单

+ @李佩轩——[宠物系统](#宠物系统)的杰出贡献者
+ @高志飞——[Pixiv](#Pixiv)功能的杰出贡献者&[RPS](#RPS)功能的杰出贡献者
+ [@cleoold](https://github.com/cleoold)——其入门教程对本项目有**启蒙**工作
+ [@Robotxm](https://github.com/Robotxm)——项目[xidian-scripts](https://github.com/Robotxm/xidian-scripts)为项目中校园系统提供帮助
+ [libxduauth](https://github.com/frankli0324/libxduauth)——提供校园账号帮助服务
+ 暂定

> 感谢他们为本项目做出的杰出贡献，再次感谢
