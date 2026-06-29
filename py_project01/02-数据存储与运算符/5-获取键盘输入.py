# 👉 1、输入与输出
# input 语句(函数)：获取键盘输入的数据，如：s = input(提示信息)
# print 语句(函数)：将数据输出到控制台，如：print(数据..)

# ⚠️ ⚠️ ⚠️，print() 默认换行。`end=` 表示每一次输出以什么结束，默认 \n，可以换成其他字符。
print('*', end=' ')   # end=' ' 表示不换行，输出空格

name = input("请输入你的名字：")
print("你的名字是：", name)
age = input("请输入你的年龄：")
print("你的年龄是：", age)

# ⚠️，无论键盘输入什么类型的数据，获取到的数据永远都是字符串类型。

print("-----------------")

# 案例：取款机取钱
total = 10000 
money = input("请输入取款金额：")
password = input("请输入密码：")
print("您已成功取出：", money, "元")

# ⚠️，int() 函数将其他类型转换为整数类型
print(f"余额：{ total - int(money) }元")

print("-----------------")

# 案例：计算器
a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
c = int(a) + int(b)
print("结果是：", c)