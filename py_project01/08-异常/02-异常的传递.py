# 1、异常的传递
# 定义：异常传递就是异常从一个作用域传递到另一个作用域，层层上报的过程。直到被捕获处理，或者传递到顶层调用者引发程序崩溃。

def func1():
    print("func1 --- running...")
    func2()

def func2():
    print("func2 --- running...")
    func3()

def func3():
    print("func3 --- running...")
    print(10/0)

try:
    func1()
except ZeroDivisionError as e:
    print("\n******")
    print("捕获到异常：",e)
    print("0不能做除数！")
    print("******\n")
else:
    print("\n******")
    print("没有出现异常！")
    print("******\n")
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")


"""
总结：⚠️⚠️⚠️
在开发复杂的程序时，我们通常会使用多层嵌套的函数调用。那么异常的最终捕获，通常放在顶层调用者中。
"""