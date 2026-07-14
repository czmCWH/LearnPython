# 👉 1、文件扩展
# 使用 open 函数操作文件时，指定的文件名可以是相对路径或绝对路径。
# - 相对路径：代表的是“运行 Python 命令时所在的终端目录（当前工作目录）”，而不是“Python 脚本文件所在的目录”。
# - 绝对路径：是从文件系统的目录开始，完整的描述文件位置的路径。
# 
# 👉 2、为了避免运行相对路径报错，有2种解决办法：
# 方法1，在终端中先切换到脚本所在目录再运行
# 方法2，在代码中使用“基于脚本所在目录”的动态绝对路径，例如：os.path.abspath(__file__) + "/file/test.txt"
# 

# 👉 2、os 模块提供了操作文件和目录的函数。
import os

def read_file():
  # open("./file/test.txt", "r", encoding="utf-8")    # 直接使用 "./file/test.txt" 相对路径，如果终端当前目录不是脚本所在目录，则会报错！
  # 获取当前脚本所在的绝对目录
  script_dir = os.path.dirname(os.path.abspath(__file__))
  # 拼接出 test.txt 的正确路径
  relative_path = os.path.join(script_dir, "file", "test.txt")
  print("====", relative_path)
  with open(relative_path, "r", encoding="utf-8") as f:
      content = f.read()
      print(content)

  print("=======================================")

  with open("/Users/CZM/Git/github/LearnPython/py_project01/09-AI应用/file/test.txt", "r", encoding="utf-8") as f:
      content = f.read()
      print(content)

read_file()

# 👉 3、操作目录
# 确认一下 Python 到底是在哪个目录下找文件的：
print("当前工作目录是:", os.getcwd())