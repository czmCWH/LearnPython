# 👉 1、Pandas 工具
# Pandas 是一个功能强大的结构化数据分析的工具集（即一个 Python 的扩展库），底层是基于 Numpy 构建的，无论是在数据分析领域、 还是大数据开发场景中都有显著的优势。
# 官网：https://pandas.pydata.org/
# 
# Pandas 的2大核心：
#   - DataFrame（类似一张表格），每一个 DataFrame 都有索引（行号）和列名，可以存储多维数据。
#   - Series（类似表格中的一列），DataFrame 中的每一列都是一个 Series 对象。
#
# 👉 2、Pandas 初体验
# 安装命令：pip3 install pandas==2.3.3
# 2.1、体验 Pandas: 
#   - 案例1：基于 Pandas 库统计班级学员的各科成绩的最高分、最低分、平均分、中位数。见 `03-Pandas入门.ipynb`。
#
# 2.2、DataFrame 的常用属性：
#   - index：每一行的索引
#   - columns：每一列的索引（即列名）
#   - values.tolist()：每一行的值，转换为列表形式
#   - dtypes：每一列数据的类型
#   - size：单元格的数量
#   - shape：行数和列数
#
# 2.3、Series 的常用属性：
#   - index：索引
#   - values：值
#   - size：单元格的数量
#   - dtype：数据类型
#   - shape：行数和列数
# 
# 
# https://www.bilibili.com/video/BV1sHU9BmEne?p=140
# 