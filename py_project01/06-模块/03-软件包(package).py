# 1、Python 软件包（package）
# 定义：软件包是模块的集合，它包含多个模块。
# 本质：一个目录，该目录中包含若干个 .py 文件。⚠️ 其中包含了一个 __init__.py 文件，用于描述当前包的信息。
# 作用：将模块组织在一起，用来管理多个模块。
# 注意，包的本质也是一个模块。


# 2、包的导入方式主要分为2类
#  - 导入包中的模块，如：
#     import 包名.模块名
#     from 包名 import 模块名1, 模块名2,...
#
#  - 直接导入包中某个模块中的内容（如：功能、变量），如：
#     from 包名.模块名 import 内容1,内容2,...
#     from 包名.模块名 import *
#
# 注意：⚠️⚠️
#   - 导入包时，Python 会自动执行 __init__.py 文件中的代码
#   - 相对路径导入、绝对路径导入均可。

# 2.1、导入 utlis 包中的 my_var.py
# from utils.my_var import *
# print(PI)
# print(NAME)

# 2.2、导入 utils 包中的 my_fun.py
# from utils import my_fun
# my_fun.log_separator1()
# my_fun.log_separator2()


# 3、导入包中默认指定的模块
# 在包的 __init__.py 文件中，可以通过定义一个特殊的变量 `__all__ = [...]` 来指定默认导入的模块。
# 当使用 from package import * 导入包时，只会导入 `__all__ = [...]` 中指定的模块。
from utils import *
print(my_var.PI)
print(my_var.NAME)
my_fun.log_separator1()
my_fun.log_separator2()

