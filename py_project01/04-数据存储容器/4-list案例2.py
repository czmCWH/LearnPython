# 案例2，合并2个列表中的元素，并对合并后的结果去重处理。
list1 = [19, 23,54, 64, 875, 20, 109, 232, 123, 54]
list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 1、合并两个列表，方法1
num = []
for i in list1:
    num.append(i)
else:
    print("list1 合并完成")

for i in list2:
    num.append(i)
else:
    print("list2 合并完成")

print("合并后的列表为：", num)

# ⚠️⚠️，合并列表，方法2
# *，解包，将列表容器拆分成一个一个的独立元素。
# 组包，将多个值合并到一个容器。
num2 = [*list1, *list2]
print("合并后的列表 num2 为：", num2)

# ⚠️⚠️，合并数组，方法3
# + 运算符，直接合并2个数组。
num3 = list1 + list2
print("合并后的列表 num3 为：", num3)


# 2、去重
new_list = []
for i in num:
    # ⚠️⚠️，in 运算符，判断元素是否在列表中，如果存在返回 True，否则返回 False；
    # ⚠️⚠️，not 取反运算符，not True 返回 False，not False 返回 True；
    if i not in new_list:
        new_list.append(i)

print("去重后的列表为：", new_list)