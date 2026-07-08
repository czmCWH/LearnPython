# 1、函数中变量的作用域
# 变量的作用域，指的是变量的作用范围（即，这个变量在哪里可以使用，在哪里不可以使用。）
# 
# 全局变量：是指在函数外部定义的变量，从定义位置开始到文件结束（包括函数内部），都可以使用。
#     - 全局变量通常定义在文件的顶部。 
#
# 局部变量：是指在函数内部定义的变量，只能在定义它的那个函数中使用。

num = 100

def fun_num():
    # ⚠️⚠️⚠️，在函数内部直接使用全局变量 num 会报错！
    # print(f"全局变量：{num}")
    # 局部变量num，只能在func函数中使用。
    num = 200
    print(f"局部变量：{num}")

fun_num()
print(f"全局变量：{num}")


# 2、函数内部使用全局变量 —— 使用 global 关键字
# global 关键字，用于明确的告诉 python 解释器，在函数内部要使用全局变量。使得在函数内部可以修改全局变量的值。
# 注意，在基于 global 关键字声明全局变量时，要先声明，再使用！

str = "hello"
def fun_str():
    global str
    str = "world"
    print(f"全局变量：{str}")

fun_str()
print(f"--- 全局变量：{str}")


# 3、建议 ⚠️
# 尽量避免在函数中使用全局变量，因为全局变量的作用域太大，容易造成混乱。
# 应当考虑使用函数参数和返回值来传递数据，而不是依赖全局变量。

# global 主要用在程序的状态、配置和计数器等场景中。 
# 调试模式开关
debug_mode = True

def enable_debug_mode():
    global debug_mode
    debug_mode = True

def disable_debug_mode():
    global debug_mode
    debug_mode = False

enable_debug_mode()
print(f"调试模式：{debug_mode}")
disable_debug_mode()
print(f"调试模式：{debug_mode}")
