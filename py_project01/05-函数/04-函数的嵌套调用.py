# 1、函数的嵌套调用
# 嵌套调用是指一个函数中调用另一个函数，即一个函数中调用另一个函数，另一个函数中又调用第三个函数，以此类推，形成一个函数调用的链条。
# 函数调用遵循栈结构，最后被调用的函数最先执行，最先调用的函数最后执行。Last in First out (LIFO), 后进先出。

def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ... before")
    print("c ... after")

function_a()

# 输出结果为：
"""
a ... before
b ... before
c ... before
c ... after
b ... after
a ... after
"""


