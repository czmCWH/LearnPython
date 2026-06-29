# 👉 1、if 条件判断
# 只有满足条件时，才会执行if后的代码块，否则跳过不执行
# 基本语法：
# if 条件表达式:
#     条件成立时，执行的代码1
#     条件成立时，执行的代码2
#     ....

# ⚠️⚠️⚠️，Python 中是通过缩进来描述代码的归属的，归属于 if 代码块的语句，需要在前方缩进 4 个空格(按Tab键 Pycharm 会自动转为空格)。

score = 700
if score > 680:
    print("欢迎您来清华大学")
print("程序结束")

print("-------------------------------")

# 👉 2、if-else 条件判断
# 基本语法：
# if 条件表达式:
#     代码块
# else:
#     代码块

age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了")
    print("可以进入网吧")
else:
    print("你还未成年")
    print("不能进入网吧")

print("-------------")

# 案例1：请用户输入一个年份，判断闰年、平年。
# 非整百年份，且能被 4 整除的年份，为闰年；
# 整百年份，且能被 400 整除的年份，为闰年；
year = int(input("请输入一个年份："))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 是平年")


print("-------------------------------")

# 👉 3、if-elif-else 条件判断
# 基本语法：
# if 条件表达式1:
#     代码块1
# elif 条件表达式2:
#     代码块2
# ...
# else:
#     代码块n

score = int(input("请输入你的成绩："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")