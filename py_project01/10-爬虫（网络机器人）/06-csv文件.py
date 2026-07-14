# 👉 1、csv 文件
# csv (Comma-Separated Values，逗号分隔值) 是一种常用、通用的文本文件格式，用于存储表格数据，可以直接使用 Excel 打开。
# csv 文件的特点：
#   1、使用逗号（⚠️，英文逗号）作为字段分隔符
#   2、使用回车换行表示记录的结束
#   3、⚠️：一个单元格多个值时，需要用双引号包裹起来
#
# 示例：
# name,age,gender
# zhangsan,18,male
# lisi,20,female
#
# Python 中操作 csv 文件有2种方式：
#   1、直接当作普通文件操作；
#   2、使用 Python 内置模块 csv；


# 🎃 方式1，直接把 csv 当作普通文件操作
import os

# 步骤1. 获取当前脚本的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 步骤2. 定义目标文件夹路径
csv_dir = os.path.join(script_dir, "csv_data")

# 步骤3. 如果文件夹不存在，则自动创建
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

def file_csv_data():
    """
    写入并读取 csv 文件数据
    """
    # 步骤1. 拼接完整的文件路径
    relative_path = os.path.join(csv_dir, "01.csv")

    # 步骤2. 写入数据到 csv 文件
    with open(relative_path, 'w', encoding='utf-8') as f:
        f.write('姓名,年龄,性别,爱好\n')
        f.write('小明,18,男,"Python,football"\n') # ⚠️：一个单元格多个值时，需要用双引号包裹起来
        f.write('小红,18,女,美食\n')
        f.write('小李,18,男,骑行\n')

    # 步骤3. 读取 csv 文件
    with open(relative_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

file_csv_data()

print('\n--------------------------------------------\n')

# 🎃 方式2，使用 Python 内置的 csv 模块
import csv

def csv_data():
    # 步骤1. 拼接完整的目标文件夹路径
    csv_file = os.path.join(csv_dir, "02.csv")

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        # 步骤2. 创建 csv writer 对象
        writer = csv.DictWriter(f, fieldnames=['姓名', '年龄', '性别', '爱好'])
        # 写入表头
        writer.writeheader()
        # 写入每一行数据
        writer.writerow({'姓名': '小明', '年龄': 18, '性别': '男', '爱好': 'Python,football'})
        writer.writerow({'姓名': '小红', '年龄': 18, '性别': '女', '爱好': '美食'})
        writer.writerow({'姓名': '小李', '年龄': 18, '性别': '男', '爱好': '骑行'})

    # 步骤2. 读取 csv 文件
    with open(csv_file, 'r', encoding='utf-8') as f:
        # 创建 csv reader 对象
        reader = csv.DictReader(f)
        for row in reader:
            print(row)  # 返回每一行的值，值类型为字典
            
csv_data()
