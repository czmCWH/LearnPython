# 👉 1、Xpath 语法
# Xpath：一种在HTML/XML文档中导航或 定位元素 的查询语言，让你能够准确的定位文档中的特定元素、属性或文本。
# 
# Xpath 语法：
#   - / 表示从文档根节点开始查找，/ 表示根节点，后面跟随查找的节点；如：/html/body/title[1] 
#   - // 表示不限定层级，不限定父节点的任意位置查找；如： //div/a/text() 
#   - ./ 表示从当前节点开始查找，已经拿到了某个节点，从这个节点的子元素中查找；如：./a/text()
#   - text() 表示提取节点的文本内容；⚠️ 获取的是直接文本，不包含内部子标签文本；如：//div/a/text() 表示提取所有 a 标签的文本内容。
#   - @ 表示匹配元素的属性值，例如：@class 表示提取 class 属性的值；如：//div/a/@href
#   - * 表示任意元素，例如：/*/text() 表示提取所有元素的文本内容。如：//div/*/text() 

import os
from lxml import html

# 🎃 步骤1，读取 resources/test.html 文件  
script_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前脚本所在的绝对目录
relative_path = os.path.join(script_dir, "resources", "仙逆人物志.html")  # 拼接出正确的路径
with open(relative_path, 'r', encoding='utf-8') as f:
    html_content = f.read() # 读取文件内容，返回一个字符串  

    # 🎃 步骤2，解析 HTML 文档，返回一个文档树对象
    doc_tree = html.fromstring(html_content)

    # 🎃 步骤3，Xpath 语法来定位元素 - 语法演示
    
    # 提取表格的所有表头文本，以列表形式返回
    th_list = doc_tree.xpath("//table/thead/tr/th/text()")  
    print(th_list)
    
    print("\n-------------------------\n")
    # td_list = doc_tree.xpath("//tbody/tr[1]/td/text()")  # 提取表格中第一行所有单元格的文本，以列表形式返回
    # td_list = doc_tree.xpath("//tbody/tr[last()]/td/text()")  # 提取表格中最后一行所有单元格的文本，以列表形式返回
    td_list = doc_tree.xpath("//tbody/tr[last() - 1]/td/text()") # 提取表格中倒数第二行所有单元格的文本，以列表形式返回
    print(td_list)

    print("\n-------------------------\n")
    # p_list = doc_tree.xpath("//p/text()")  # 提取所有段落文本，以列表形式返回。
    # p_list = doc_tree.xpath("//p[@class]/text()")  # 提取所有带有 class 属性的段落文本，以列表形式返回。
    p_list = doc_tree.xpath("//p[@class='xn']/text()")  # 提取所有 class 为 xn 的段落文本，以列表形式返回。
    print(p_list)

    print("\n-------------------------\n")
    ta_list = doc_tree.xpath("//thead/tr/*/text()")  # * 表示任意元素，提取表头中所有元素的文本，以列表形式返回。
    print(ta_list)

    print("\n-------------------------\n")
    # tc_list = doc_tree.xpath("//td/img/@src")  # @ 表示属性，提取所有 img 标签的 src 属性的值，以列表形式返回。
    tc_list = doc_tree.xpath("//td/img/@*")  # 提取所有 img 标签的所有属性，以列表形式返回。
    print(tc_list)