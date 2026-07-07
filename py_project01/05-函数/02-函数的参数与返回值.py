# 1、函数的参数与返回值
#
# 函数定义时如果有多个参数，多个参数之间使用逗号分隔。在调用函数时，也需要传递相应的参数。
# return 返回值：函数执行后，返回的结果。
# 
# 形参（形式参数）：函数定义时，括号中的参数。只能在函数内部使用。
# 实参（实际参数）：函数调用时，实际传入的参数。

# 计算圆的面积
def area_of_circle(r):
    s = 3.14 * r**2
    return s

area = area_of_circle(4)
print(f"半价为4圆的面积为 {area}")

# 计算长方形的面积
def area_of_rectangle(l, w):
    s = l * w
    return s

area = area_of_rectangle(6, 8)
print(f"6x8 矩形的面积为 {area}")

print("-----------------------------")

# 2、函数多个返回值
# 函数多个返回值会自动封装为元组返回

# 计算圆的周长和面积
def circle(r):
    c = round(2 * 3.14 * r, 2)  # 保留两位小数
    s = round(3.14 * r**2, 2)   # 保留两位小数
    return c, s

cl = circle(5)
print(f"半径为5的圆的周长是{cl[0]}, 面积是{cl[1]}")

# 解包元组
c, s = circle(5)
print(f"半径为5的圆的周长是{c}, 面积是{s}")
