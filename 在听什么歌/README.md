# 在听什么歌

这个插件获取了你电脑的SMTC信息，一般大多数的播放软件都支持此协议，此协议只在**Windows10**及以上操作系统存在，**网易云音乐**或许需要安装插件来支持SMTC。

## 安装

1. 将`getSMTCinfo.plugin` 和 `getSMTCinfo_api.py`放入99微信机器人的`plugin`文件夹下

2. 使用pip安装本插件所需要的库

~~~bash
pip install -r requirements.txt
~~~

## 自定义

您可以在`getSMTCinfo_api.py`修改关键词，`getSMTCinfo.plugin`本质上是一个Python程序，为了绕过主程序的检查而这么做，您可以在终端执行下面的命令来检查是否安装正常

```bash
python getSMTCinfo.plugin
```

在`getSMTCinfo.plugin`中修改机器人要发送的内容

---------------

# What Are You Listening To?

This plugin retrieves SMTC (System Media Transport Controls) information from your computer. Most media players support this protocol, which is only available on **Windows 10** and later operating systems. **NetEase Cloud Music** may require an additional plugin to support SMTC.

## Installation

1. Place `getSMTCinfo.plugin` and `getSMTCinfo_api.py` into the `plugin` folder of the 99 WeChat robot.
2. Use pip to install the required libraries for this plugin:

```bash
pip install -r requirements.txt
```

## Customization

You can modify the keywords in `getSMTCinfo_api.py`. Essentially, `getSMTCinfo.plugin` is a Python program designed to bypass the main program's checks. You can run the following command in the terminal to verify if the installation is successful:

```bash
python getSMTCinfo.plugin
```

Modify the content that the robot will send in `getSMTCinfo.plugin`.