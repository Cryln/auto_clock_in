# 东百大学，自动打卡

写这个的初衷，其实不是为了方便，而是偶然间看到个叫playwright的python库，挺好玩的

也能实现网页操作的自动化，但是其原理还是模拟各种事件，去触发js。我觉得不ok

所以，就希望通过直接与服务端通信报文来做，也就是“网络爬虫”，很遗憾我没能选上python选修课，自能自学了

主要想推荐那些对这方面感兴趣的萌新一个工具Postman，还有chrome的devtools

我不知道有没有其他好用的工具，我只用过这个，挺好使的

postman可以通过一个chrome插件记录下所有的post，get请求，能够让你很快理解网页的通讯细节，因为javaweb课上学过一些，所以还不算特别难


## 使用方法
### 本人上报 
```shell
python daka.py [学号] [密码] 
#例如：
python daka.py 20182333 abc123
```
### 或者替别人上报
```shell
python daka.py [学号] [密码] [被上报人学号] [被上报人姓名]
#例如：
python daka.py 20182333 abc123 20186666 佩奇
```
> 如果你的电脑还有python 2.x ， 那你可能要使用 python3 来运行命令
### 使用 Github Actions 自动上报
+ fork your own copy of this repository to your account
+ set secrets{ USERNAME: [学号], PASSWORD:[密码] }
+  ~~更多的我就不太清楚了，我也没试过folk别人的action，可能还需要在Actions页设置，细节在/.github/workflow/main.yml,防止意外，我是每2个小时自动打卡~~
+ 用室友账号试了一下：先fork，再去Actions里允许运行workflow，在点开项目Settings >> Secrets >> new repository secret。分别添加USERNAME,PASSWORD, value就是你的学号，密码。 

TODO:
想用js来实现，又是偶然看到iPad/iOS上的快捷指令支持JavaScript，可以放进Safari运行。但是我js有点菜