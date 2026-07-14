# 👉 案例：获取 TIOBE 编程语言排行榜  
# https://www.tiobe.com/tiobe-index/
#
# 实现功能：
#   - 使用 lxml 库解析网页内容。需参看网页源代码，确定需要提取的数据对应的 Xpath 表达式。
# 

import requests
from lxml import html

# 1. 发送请求，获取网页内容
url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
html_str = response.text

# 2. 解析网页内容
doc_tree = html.fromstring(html_str)

# 3. 提取数据

# 1、提取 top20 表格中的所有表头文本
th_list = doc_tree.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

print("\n-------------------------\n")

# 2、提取编程语言 top20 表格中所有行的数据
tr_list = doc_tree.xpath("//table[@id='top20']/tbody/tr") # 获取所有行 <tr> 元素
for tr in tr_list:
    td_list = tr.xpath("./td/text()")   # 获取当前行 <tr> 的所有单元格 <td> 文本
    print(td_list)


# ⚠️⚠️⚠️ 可以直接在浏览器中复制 Xpath 表达式：
#   - 在浏览器中选择网页 元素 -> 右键选择 "审查元素" -> 右键选择 "复制" -> 选择 "拷贝 Xpath"
#   - 粘贴到 Xpath 测试工具中，测试 Xpath 表达式是否正确
