# 👉 1、嵌套循环
# 以 for 循环为例，嵌套循环就是在 for 循环中再嵌套一个 for 循环。
# 语法结构如下：
# for 变量1 in 可迭代对象1:
#     for 变量2 in 可迭代对象2:
#         循环体语句1
#         循环体语句2
#         ...
#         循环体语句n
#     else:
#         循环正常结束后的操作

# 案例1：打印三角形
for i in range(1, 10):
    for j in range(i):
        print('*', end=' ')   # ⚠️，print() 默认换行，end=' ' 表示输出结尾用 空格代替换，不换行。
    print()   # 外层循环结束后换行  
else:
    print("循环正常结束")

# 案例2：打印九九乘法表
# 外层循环控制输出行；内层循环控制每行的列数
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i*j}", end='\t')   # end='\t' 表示输出结尾用 制表符代替换，不换行。
    print()   # 外层循环结束后换行
else:
    print("循环正常结束")

