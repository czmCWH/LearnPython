# 1、异常
# 定义：异常（也称 bug）是指在程序执行过程中出现的错误，它会中断程序的正常执行流程。
# 作用：
#     1. 阻止程序继续执行。保证数据、逻辑的正确性，避免程序执行混乱。
#     2. 提供错误信息。在开发阶段，尽量发现更多的问题，尽早解决问题，保障程序正常执行。
#
# 异常是编写健壮程序的重要工具。
#




# 2、异常处理
# 程序运行过程中出现异常，有2种处理方案：
#   1、不处理，整个程序因为一个 Bugs 而崩溃，中断执行。
#   2、捕获异常，按照我们自己的处理方式，处理完异常，程序继续执行。
# 
# 捕获异常的语法：
# try:
#     可能产生异常的代码1
#     可能产生异常的代码2
#     ...
# except 异常类型1 as 变量名:
#     处理异常的代码1
# except 异常类型2 as 变量名:
#     处理异常的代码2
#     ...
# else:
#     没有出现异常时，执行的代码块。
# finally:
#     无论是否出现异常，都会执行这里的代码。通常用于释放资源，比如关闭文件。
#


# 1、示例，捕获未定义的变量异常 —— NameError
try:
    print(my_name)
    print(my_age)
except NameError as e:
    print("\n******")
    print("捕获到异常：",e)
    print("访问了未定义的变量！")
    print("******\n")
else:
    print("\n******")
    print("没有出现异常！")
    print("******\n")
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")

print("------------------------------------------------")

# 2、示例，捕获除零异常 —— ZeroDivisionError
try:
    num = 10 / 0
except ZeroDivisionError as e:
    print("\n******")
    print("捕获到异常：",e)
    print("0不能做除数！")
    print("******\n")
else:
    print("\n******")
    print(f"结果是：{num}")
    print("******\n")
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")

print("------------------------------------------------")

# 3、示例，捕获数组越界异常 —— IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError as e:
    print("\n******")
    print("捕获到异常：",e)
    print("数组越界了！")
    print("******\n")
else:
    print("\n******")
    print("没有出现异常！")
    print("******\n")
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")


print("------------------------------------------------")

# 4、示例，捕获输入非数字异常 —— ValueError
try:
    num = int(input("请输入一个整数："))
except ValueError as e:   # 捕获 ValueError 类型的异常，并把异常信息赋值给变量 e
    print("\n******")
    print(f"捕获到异常：{e}")
    print("你输入的不是数字，请重新运行程序！")
    print("******\n")
else:
    print("\n******")
    print(f"输入的是：{num}")
    print("******\n")
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")

print("------------------------------------------------")

# 3、 Exception 是所有内置异常的基类。
# 捕获 Exception 类型的异常，可以捕获所有内置的异常。
try:
    print(my_name)
    print(10/0)
except NameError as e:
    print("捕获到异常：",e)
except Exception as e:  # ⚠️⚠️⚠️，捕获所有类型的异常，并把异常信息赋值给变量 e
    print("捕获到异常：",e)
finally:
    print("### 无论是否出现异常，都会执行 finally 代码块 ###")



















































































































































