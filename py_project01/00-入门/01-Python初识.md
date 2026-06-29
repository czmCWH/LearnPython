# 一、Python初识

Python 是荷兰计算机科学家 吉多.范罗苏姆 (Guido van Rossum, 龟叔) 在 1991 发布的一门语法简单、容易上手的编程语言。


# 二、Python 环境准备

## 2.1、Python 解释器

* 1、安装 Python 解释器
	- 官网 <https://www.python.org/> -> 【Downloads】-> 最新版本 `Python 3.14.6`。
	- 【Downloads】-> Mac OS -> 下载 `Python 3.13.10`。
	- 双击下载好的 .pkg 软件安装包，一路点击“继续”和“同意”，直到提示安装成功。

> 注意，一般不使用官网最新版本，因为使用的资源库可能未适配最新版本。


* 2、验证安装是否成功

```shell
# 检查 Python 版本
$ python3 --version
Python 3.13.10

# 检查包管理器
$ pip3 --version
pip 25.3 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
```

> ⚠️，Mac 系统可能自带轻量级环境，务必使用 python3 而不是 python 关键字。


* 3、终端中编写 Python 第一行代码

```shell
# 直接输入 python3 回车，进入到 python 解释器
$ python3
Python 3.13.10 (v3.13.10:4fd884356d7, Dec  2 2025, 09:31:05) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> print("Hello Python")
Hello Python

# 退出 Python 解释器
>>> exit()
```

* 4、终端中执行 Python 代码文件
在终端中每编写一行 Python 代码敲回车会自动执行，如果想一次性执行多行 Python 代码，可以将多行 Python 代码定义在一个 `.py` 文件中，然后在终端运行这个文件。

定义 hello.py 代码文件：
```python
print("################")
print("Hello World!")
print("################")
print("Hello Python!")
```

运行文件：

```shell
$ python3 /Users/chen/Desktop/hello.py 
################
Hello World!
################
Hello Python!
```



## 2.2、Python 开发工具
Python 程序的开发工具有很多，常见的有 VSCode、PyCharm 等常用的 IDE，而 PyCharm 是使用的最为广泛的 Python 开发工具。

> IDE：集成开发环境(Integrated Development Environment)，是集成了代码编写功能、分析功能、调试功能等一体化的集成环境的开发软件


* 1、安装 PyCharm

PyCharm 是Jetbrains公司旗下的一款用于Python程序开发的IDE。

下载地址：<https://www.jetbrains.com/pycharm/download>


PyCharm 是永久免费，另赠送一个月专业版。安装包有 1GB。

> 建议所有的软件安装放在 `develop` 目录下。


* 2、使用 PyCharm 创建 Python 项目目录结构

- `.idea` 目录，保存项目的配置信息。
- `.venv` 目录，虚拟环境，保存项目的环境信息。即当前项目依赖的工具和文件。

> 通过虚拟的运行环境 `.venv`，可以保证每一个 Python 项目都在一个相对独立的隔离的运行环境中运行，项目与项目之间互不影响。





