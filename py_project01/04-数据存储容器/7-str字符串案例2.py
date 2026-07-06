# 案例2 —— 回文数判断
# 输入一个字符串，判断该字符串是否是回文(两边对称)。
text = input("请输入一个字符串：")
if text == text[::-1]:
    print("是回文")
else:
    print("不是回文")


# 案例3
# 将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
list = []
for i in range(10):
    str = input(f"请输入第{i + 1}个字符串")
    list.append(str[::-1].upper())
else:
    print(list)