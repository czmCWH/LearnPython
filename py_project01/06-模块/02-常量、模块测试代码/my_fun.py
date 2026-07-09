# 1、常量
# 定义：常量就是一旦赋值之后就不能修改的值。
# 常量通常使用大写字母表示

# 定义常量
PI = 3.1415926
NAME = "Python哥"

# 2、定义日志分隔符函数
def log_separator1():
    print("- " * 30)    # 打印30个"-"

def log_separator2():
    print("+ " * 30)    # 打印30个"+" 

def log_separator3():
    print("# " * 30)    # 打印30个"#"

def log_separator4():
    print("= " * 30)    # 打印30个"*"



# ⚠️⚠️⚠️，当模块被导入时，模块中的代码会被执行。
log_separator1()


# 2、问题：如何保证模块的一些测试代码，在模块被导入时不被执行？
# __name__，是 Python 中的内置变量，表示当前模块的名字。
# 当模块被直接运行时，__name__ 的值为 "__main__"。
# 当模块被导入时，__name__ 的值不是 "__main__"。
# 因此，可以通过判断 __name__ 的值来决定是否执行模块中的测试代码。
if __name__ == "__main__":
    log_separator2()
    print(PI)
    log_separator3()
    print(NAME)
    log_separator4()
else:
    print("模块被导入")


# 3、__all__，指定通过 from module import * 导入的内容，即 * 表示的内容
__all__ = ["log_separator1", "log_separator2"]