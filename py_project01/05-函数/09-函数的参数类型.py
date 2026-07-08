# 1、函数的参数类型
# 普通参数：字符串、数字、布尔值、列表、元组、集合、字典等。
# 特殊参数：函数参数。

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("除数不能为0")
    else:
        return x / y


def calc(x, y, oper):
    """
    计算函数
    
    :param x: 第一个参数
    :param y: 第二个参数
    :param oper: 操作函数，⚠️，这是一个函数参数，不是普通的参数类型。
    """
    return oper(x, y)

v1 = calc(10, 5, add)
print("加：", v1)
v2 = calc(10, 5, subtract)
print("减：", v2)
v3 = calc(10, 5, multiply)
print("乘：", v3)
v4 = calc(10, 5, divide)
print("除：", v4)