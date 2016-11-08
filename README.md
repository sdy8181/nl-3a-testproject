# 专为公司开发的自动化测试平台，用于车载娱乐系统的测试
## 介绍
测试工具客户端
提供界面方便测试人员选择步骤来组织测试场景，并选择要运行的测试场景进行测试，测试结束可直接查看测试报告

测试工具服务端
向客户端提供测试用例编写需要的测试步骤信息，保存测试场景到数据库等

测试脚本工程
测试场景执行的胶水代码，采用BDD框架

## 采用语言和工具
python3.4
behave
pyqt5.5.1
uiautomator(python)
flask
JDK

#QGATP环境部署
##服务端部署
** 一般测试人员无需关注，只需要关注服务端的IP和端口即可**
###环境准备
####所需软件
* python3.4+

###部署步骤
#### 创建虚拟环境
> 进入放置服务端代码的目录下执行以下命令
> mkdir atps
> python -m venv flask

#### 安装环境所需要的库
##### windows用户
> cd atps
> 下载最新服务端代码并放在flask同级目录下
> $flask\Scripts\pip.exe -r install requirements.txt

##### linux用户
> cd atps
> 下载最新服务端代码并放在flask同级目录下
> $flask\bin\pip  -r install requirements.txt

##### 启动服务端
1 修改run.py文件中的ip地址配置
2 windows用户在atps目录下运行 $flask\Scripts\python.exe run.py
3 linux用户在atps目录下运行 $flask\bin\python run.py

##客户端部署
###环境准备

####所需软件
* python3.4+(以下安装均使用pip install \*\*\*)
>* requests
>* behave
>* pillow
>* pyserial
>* GitPython
>* uiautomator
>* PyQt5
* jdk
* git

###部署步骤(以上软件都均已正确安装)
1 下载地址：
> * 客户端： http://github.com/ouguanqian/atpc.git
> * 测试脚本： http://github.com/ouguangqian/autotestproject.git

2 新建文件夹atp
3 将下载下来的atpc和autotestproject放在atp目录下
4 进入atpc目录
5 命令行执行命令$ python run.py或者双击start.bat打开客户端应用

##客户端使用
### 使用地图
*** 登录\-\-\>设置\-\-\>新建用例\-\-\>选择用例并执行\-\-\>查看报告 ***

###登录并设置
1 打开客户端程序进入登录界面
![登录界面截图](http://a.hiphotos.baidu.com/image/pic/item/79f0f736afc3793132f70ae9e3c4b74542a91156.jpg)

2 点击'服务器设置'设置服务器IP和端口
![服务器设置界面](http://e.hiphotos.baidu.com/image/pic/item/7e3e6709c93d70cfc71924cdf0dcd100bba12b0b.jpg)

3 输入用户名和密码即可进入系统主界面
![系统主界面](http://b.hiphotos.baidu.com/image/pic/item/7e3e6709c93d70cfc25921cdf0dcd100bba12b4b.jpg)

4 打开菜单栏 '设置|应用设置'，进入‘应用设置’界面,设置后保存
![应用设置界面](http://a.hiphotos.baidu.com/image/pic/item/d058ccbf6c81800ac16177ceb93533fa838b476e.jpg)
> * 脚本目录: 填写存放测试工程的目录路径
> * 服务器Ip:填写服务器的ip地址，和登录配置的一致, 如：10.10.99.35
> * 服务器Port:填写服务器的启动端口，默认：5000
> * 测试脚本的git地址：服务器上git地址，下拉框选择，方便更新测试脚本

5 打开菜单 '设置|脚本设置'，进入’脚本设置‘界面，设置后保存
![脚本设置界面](http://c.hiphotos.baidu.com/image/pic/item/6d81800a19d8bc3e6bbbf80a8a8ba61ea9d345bb.jpg)
> * 音频播放器路径: 本地播放器执行文件的路径。 PS:路径加入到path中，并设置播放一段音频后停止，建议使用foobar2000
> * 音频文件路径: 本地音频文件存放路径，用于测试语音场景的录音文件
> * 运行日志存放路径: 用例运行过程中产生的失败截图路径
> * 车机设备编号: 车机的serialnum，通过命令行adb devices获取
> * 车机IP地址: 车机的IP地址
> * 车机PCAN波特率: 车载数据传输速率
> * 手机设备编号: 手机的serialnum，通过命令行adb devices获取
> * 手机蓝牙名称: 手机蓝牙的名字， 用于测试蓝牙场景连接蓝牙
> * 测试版本编号: 默认即可(后续会废除)
> * usb音乐名列表: u盘音乐中的音乐名称，英文逗号分隔，用来测试U盘音乐，判断当前播放的音乐是否为U盘音乐

###添加编辑用例
####用例编辑界面介绍
点击主界面的’添加‘按钮，进入’用例编辑‘界面
![用例编辑界面](http://f.hiphotos.baidu.com/image/pic/item/0824ab18972bd407886afa7d73899e510eb30984.jpg)
* 用例名称: 不为空，并且唯一，有重复会有错误提示
* 用例类型: 必选，选择用例场景类型，如：基本类型等，用于快速筛选用例,可在下拉框最下方点击添加新用例类型
* 所属模块：必选，选择用例所测试的模块，如：音乐，视频等，用于快速筛选用例,可在下拉框最下方点击添加新模块类型
* 上移，下移，删除是针对用例步骤的操作，选中用例步骤就可以调整步骤顺序或者删除操作
* 左侧列表为所有的用例步骤信息，可以通过上面的下拉框来筛选操作的步骤和验证的步骤，也可以通过搜索框，根据关键字搜索对应的步骤信息
* 中间单列表格为展示用例的步骤信息，步骤按照操作顺序来组合用例
* 右边表格展示步骤的参数信息，包括参数名称，参数值

####添加用例
1 填写用例名称，用例类型，所属模块等信息
> * 用例名称必须保证唯一性，如果为空或者不唯一，界面会有提示信息
> * 用例类型和所属模块下拉框选择，如果没有所需要的类型，可在下拉框底部点击'\-\-新类型\-\-'或'\-\-新模块\-\-'添加

2 最左侧的为所有的用例步骤信息,可以通过下拉框和关键字快速筛选所需要的用例步骤信息
3 双击要添加的步骤，就会添加步骤到中间的用例表格中
4 选中要调整的用例步骤，选择相应的操作(上移，下移，删除)
5 选中用例步骤，如果步骤需要填写参数，在右侧的表格中会出现参数信息，在参数值表格中填写具体值并回车保存
> * 单步次数为该步骤单步循环执行的次数，如果不填，默认为:1
> * 如果有的参数名为o\_result,意为该步骤会有结果返回，参数值务必用'o_’开头如下图
![有返回值的步骤参数](http://g.hiphotos.baidu.com/image/pic/item/21a4462309f79052c6a4a5fe04f3d7ca7acbd5b3.jpg)

6 点击保存按钮保存用例
7 回到主界面，点击顶部的刷新按钮，即可看到新添加的用例信息

####编辑用例
1 在主界面，双击用例名称即可打开‘用例编辑’界面
2 编辑用例的用例名称不可更改，如果要更改的话，需要先删除再新建，如果有需要可放开这个限制
3 用例编辑可参照添加用例操作
4 用户只能编辑自己编写的用例，非自己编写的用例只能查看不能修改和删除

###删除用例
1 在主界面选中要删除用例的复选框，点击‘删除’按钮即可删除所选用例
2 用户只能删除自己编写的用例，非自己编写的用例不可删除

###执行用例
1 点击主界面顶部的‘筛选>>>’展开筛选选项，点击‘筛选<<<’收回
2 通过主界面顶部的用例类型,所属模块和人员分类快速筛选用例，或者用例搜索框来筛选用例
3 选中要执行的用例前的复选框
4 设置用例执行次数（默认是一次），点击‘运行’按钮即可执行用例
5 在主界面下方的执行历史列表可看到当前用例执行状态
![筛选界面](http://f.hiphotos.baidu.com/image/pic/item/b90e7bec54e736d18a6f6dc893504fc2d46269f6.jpg)

###查看用例执行结果
1 点击主界面中‘执行历史列表’指定任务的查看单元格即可打开执行结果展示界面，如下图:
![结果查看界面](http://f.hiphotos.baidu.com/image/pic/item/6a63f6246b600c335a578f6f124c510fd9f9a16f.jpg)
2 如果用例执行失败或者用例执行中，界面会提示相应的错误信息，如下图:
![用例执行失败截图](http://e.hiphotos.baidu.com/image/pic/item/9213b07eca80653820f0a5939fdda144ad348213.jpg)
3 如果用例执行成功，将会看到用例汇总信息，成功的用例(绿色展示)，失败的用例(红色展示)
4 双击用例名称获取前面的三角图形，会看到具体用例步骤信息和错误信息
5 点击‘下载报告’按钮，并指定报告存放路径(包含文件名),即可本地查看测试报告信息

###查看自动化测试持续集成
1 点击主界面右上角的‘持续集成’按钮，即可跳转持续集成界面，如下图:
![持续集成截图](http://b.hiphotos.baidu.com/image/pic/item/d0c8a786c9177f3e56224a8e78cf3bc79f3d561a.jpg)

##QA
1 在选中用例运行的过程中在客户端终端会报以下错误
>   File "c:\users\shenshun\appdata\local\programs\python\python35\lib\site-packag
es\behave\runner.py", line 303, in exec_file
    code = compile(f.read(), filename2, 'exec')
UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 397: illegal
multibyte sequence
> 解决方法：
> 打开错误中指定的文件runner.py在303行附近修改如下代码
with open(filename) as f:改为 with open(filename, encoding='utf-8') as f:

2 在执行有输入框的用例，会遇到无法输入内容
> 解决方法：在车机上安装utf7ime.apk输入法并设置为默认输入法即可
> 设置默认输入法命令:
adb shell settings put secure default_input_method jp.jun_nama.test.utf7ime/.Utf7ImeService
> 还原擎感输入法命令:
adb shell settings put secure default_input_method com.android.inputmethod.qingganime/.QingganIME

3 在用例运行过程中会出现如下错误：
> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\shenshun\AppData\Local\Programs\Python\Python35\lib\site-packag
es\git\repo\base.py", line 966, in clone_from
    return cls._clone(git, url, to_path, GitCmdObjectDB, progress, **kwargs)
  File "C:\Users\shenshun\AppData\Local\Programs\Python\Python35\lib\site-packag
es\git\repo\base.py", line 907, in _clone
    v=True, **add_progress(kwargs, git, progress))
  File "C:\Users\shenshun\AppData\Local\Programs\Python\Python35\lib\site-packag
es\git\cmd.py", line 466, in <lambda>
    return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)
  File "C:\Users\shenshun\AppData\Local\Programs\Python\Python35\lib\site-packag
es\git\cmd.py", line 910, in _call_process
    return self.execute(make_call(), **_kwargs)
  File "C:\Users\shenshun\AppData\Local\Programs\Python\Python35\lib\site-packag
es\git\cmd.py", line 630, in execute
    raise GitCommandNotFound(str(err))
git.exc.GitCommandNotFound: [WinError 2] 系统找不到指定的文件。<br>
> *解决方法*：是因为本机没有安装git，需要在本机安装git

##联系我们
Email：guangqianou@pateo.com.cn(欧光乾)，zhiyuanwang@pateo.com.cn(王志远)