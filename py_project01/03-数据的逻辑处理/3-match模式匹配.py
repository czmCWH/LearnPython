# 👉 1、match-case 结构模式匹配
# 结构模式匹配就是用一个清晰的 模板 去精准的匹配 数据 的结构和内容，匹配成功 则执行响应的操作。
# 结构模式匹配的语法格式如下：
# match 变量名:
#     case 模式1:
#         代码块1
#     case 模式2:
#         代码块2
#     ...
#     case _:
#         默认代码块

# ⚠️，match-case 结构模式匹配，只支持 Python 3.10 及以上版本

num = input('请输入一个数字：')
match num:
    case '1':
        print('今天是周一，需要上班')
    case '2':
        print('今天是周二，需要上班')
    case '3':
        print('今天是周三，需要上班')
    case '4':
        print('今天是周四，需要上班')
    case '5':
        print('今天是周五，需要上班')
    case '6' | '7':   # ⚠️ ⚠️ ⚠️  匹配多个模式, 使用 | 分隔，表示或关系。
        print('今天是周末，可以休息')
    case _:           # ⚠️ ⚠️ ⚠️  默认匹配，当所有模式都不匹配时，执行默认代码块。
        print('输入错误')

print('---------------')

# 案例1，通过 match-case 结构模式匹配，进行加减乘除运算
num1 = float(input('请输入第一个数字：'))
num2 = float(input('请输入第二个数字：'))
operator = input('请输入运算符号（+ - * /）：')
match operator:
    case '+':
        print(f"{num1} {operator} {num2} = {num1 + num2}")
    case '-':
        print(f"{num1} {operator} {num2} = {num1 - num2}")
    case '*':
        print(f"{num1} {operator} {num2} = {num1 * num2}")
    case '/' if num2 != 0:    # ⚠️ ⚠️ ⚠️  使用 if 语句进行条件判断，如果 num2 不等于 0，则执行代码块。
        print(f"{num1} {operator} {num2} = {num1 / num2}")
    case _:
        print('操作不支持！！！')

print('---------------')

# 案例2，通过 match-case 结构模式匹配 判断用户输入的月份，并输出相应的季节。
month = int(input('请输入月份（1~12）：'))
match month:
    case 1 | 2 | 12:
        print('冬季')
    case 3 | 4 | 5:
        print('春季')
    case 6 | 7 | 8:
        print('夏季')
    case 9 | 10 | 11:
        print('秋季')
    case _:
        print('输入错误')

print("-------------------------------")

# 👉 2、match-case 应用场景
# match：基于某个变量的多个固定值进行分支判断时，可以使用 match 模式匹配；
# if：条件判断涉及复杂的逻辑判断、范围比较、组合条件判断时；


