# 1、默认参数值
# 在定义函数时，可以给形参提供默认的值，在调用函数时，可以不传递有默认值的参数。
# 注意⚠️：
#   - 默认参数值，必须放在没有默认值的参数之后。
#   - 函数定义中可以有多个默认参数值。
#   - 如果默认参数不传实参，则使用默认值；如果传了实参，则覆盖默认值。

def fun_default(name, age=18, gender="未知", city="火星"): 
    print(f"姓名：{name}, 年龄：{age}, 性别：{gender}, 城市：{city}")

fun_default("张三", 25)

print("------------------------------\n")

# 2、不定长位置参数 —— *args
# 定义：是指传递任意数量的位置参数，这些参数会被收集到一个名为 args 的 “元组” 中。args 只是约定俗成的变量名。
# 语法：def 函数名(*形参名)

def fun_var(*args):
    print("不定长参数的个数: ", len(args))
    print("不定长参数的第一个值: ", args[0]) 
    for arg in args:
        print(arg)

fun_var("苹果", "香蕉", "橙子")

def fun_calc(*args):
    min_value = min(args)
    max_value = max(args)
    avg_value = round(sum(args) / len(args), 2)   # ⚠️ 计算平均值，保留两位小数
    return min_value, max_value, avg_value

min_v, max_v, avg_v = fun_calc(11, 2, 3, 4, 5, 22)
print("最小值: ", min_v)
print("最大值: ", max_v)
print("平均值: ", avg_v)

print("------------------------------\n")

# 3、不定长关键字参数（**kwargs）：
# 定义：传递任意数量的关键字参数，这些参数会被收集到一个名为 kwargs 的 “字典” 中。kwargs 只是约定俗成的变量名，keyword args。
# 语法：def 函数名(**形参名)

def fun_var2(**kwargs):
    print("不定长关键字参数的个数: ", len(kwargs))
    for key, value in kwargs.items():
        print(f"{key} = {value}")

fun_var2(name="张三", age=25, gender="男")

print("------------------------------\n")

# 4、不定长位置参数、不定长关键字参数的混合使用
# 语法：def 函数名(*args, **kwargs)
# 注意⚠️：
#   - 不定长位置参数，必须放在不定长关键字参数之前。
#
def fun_mix(*args, **kwargs):
    """
    根据传入的不定长位置参数，计算最小值、最大值、平均值；根据传入的不定长关键字参数，决定操作行为
    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
    """
    mix_value = min(args)
    max_value = max(args)
    avg_value = sum(args) / len(args)

    # 根据关键字参数，决定是否对平均值进行小数点处理
    if kwargs.get("round") is not None:
        avg_value = round(avg_value, kwargs.get("round"))
    
    # 根据关键字参数，决定是否打印
    if kwargs.get("print"):
        print(f"最小值：{mix_value}, 最大值：{max_value}, 平均值：{avg_value}")

    return mix_value, max_value, avg_value

fun_mix(11, 2, 3, 4, 5, 6, 7, round=3, print=True)
print("--- 下一次调用 ---")
min_v, max_v, avg_v = fun_mix(11, 2, 3, 4, 5, 6, 7)
print(f"最小值：{min_v}, 最大值：{max_v}, 平均值：{avg_v}")


"""
总结⚠️
*args 不定长位置参数：适用于处理数量不确定的数据。—— 重点在数据
*kwargs 不定长关键字参数：适用于处理数量不确定的选项。即，函数的配置参数，用来定制函数的行为。—— 重点在选项配置
"""
