# 👉 1、网页解析
# 网页解析：是指从原始HTML文档中提取数据的过程，也是网络爬虫的关键步骤，从一堆标签文本中提取出需要的数据。
#
# lxml 库：是一个高性能的HTML/XML文档的解析库，支持基于 Xpath 语法来解析和获取网页数据。
# 安装：pip3 install lxml
# 
# Xpath 语法：是一种用于在HTML/XML文档中导航或定位元素的查询语言，类似于CSS选择器。Xpath 能够准确的定位文档中的特定元素、属性或文本。
#

import os
from lxml import html

# 🎃 步骤1，读取 resources/test.html 文件  
script_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前脚本所在的绝对目录
relative_path = os.path.join(script_dir, "resources", "仙逆人物志.html")  # 拼接出正确的路径
with open(relative_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
    # print(html_content)

    # 🎃 步骤2，解析 HTML 文档，返回一个文档树对象
    doc_tree = html.fromstring(html_content)

    # 🎃 步骤3，使用 Xpath 语法来定位元素，提取指定的数据
    # / 表示从文档根节点开始查找 ；
    # // 表示不限定层级，不限定父节点的任意位置查找；
    # ./ 表示从当前节点开始查找，已经拿到了某个节点，从这个节点的子元素中查找；
    # text() 表示提取节点的文本内容；
    thead_list = doc_tree.xpath("//table/thead/tr/th/text()")  # 提取表格的所有表头文本，以列表形式返回
    print(thead_list) # 打印：['姓名', '性别', '头像', '修为', '技能', '身份地位', '师承', '法宝']

    print("\n-------------------------\n")

    # 提取表格中指定行的数据
    # tr[2] 表示提取第二个tr元素，索引从1开始计数；
    tr_list = doc_tree.xpath("//table/tbody/tr[2]/td/text()")  # 提取表格中第二行的所有单元格文本，以列表形式返回
    print(tr_list) # 打印：['林动', '男', '林动的头像链接', '不详', '不详', '不详', '不详', '不详']

    print("\n-------------------------\n")

    # 提取表格的所有行数据
    tbody_list = doc_tree.xpath("//table/tbody/tr") # 提取表格的所有行元素，以列表形式返回
    for tr in tbody_list: # 遍历所有行元素
        td_list = tr.xpath("./td/text()")  # 提取当前行的所有单元格文本，以列表形式返回
        print(td_list)
