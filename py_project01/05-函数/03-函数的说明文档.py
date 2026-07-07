# 1、函数的说明文档
# 函数的说明文档(Docstring)是写在函数开头，用三个引号包裹的字符串，用于解释函数的功能、参数、返回值等信息，方便调用者清楚函数的具体作用及细节。

def circle(r):
    """
    根据圆的半径，计算圆的周长和面积
    
    :param r: 圆的半径

    :return: 圆的周长和面积
    """
    c = round(2 * 3.14 * r, 2)  # 保留两位小数
    s = round(3.14 * r ** 2, 2)  # 保留两位小数
    return c, s


def rectangle(length, width):
    """
    根据长方形的长和宽，计算长方形的周长和面积

    :param length: 长方形的长

    :param width: 长方形的宽

    :return: 长方形的周长和面积
    """
    c = 2 * (length + width)
    s = length * width

# 2、查看函数的说明文档
# 方式1，help(函数名)，如：help(print)
help(circle)

print("-------------------------------")

# 方式2，鼠标悬停在函数名上，查看提示信息 —— 推荐
