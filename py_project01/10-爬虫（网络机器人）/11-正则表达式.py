# 👉 1、正则表达式
# 正则表达式（Regular Expression）是一种由特定语法规则组成的文本模式，用来描述、匹配字符串中符合特定规则的字符序列。
# 就相当于一种模式匹配工具，允许用户通过简介的语法进行复杂文本的搜索、匹配、提取和替换工作。
# 
# Python 中使用正则表达式，需要导入 re 模块。
#

# 👉 2、re 模块常用函数
# re 模块的常用函数：
#   - re.match(pattern, string)：根据 pattern 正则表达式从字符串的开头开始匹配，如果找到返回 Match 对象，否则返回 None。
#   - re.search(pattern, string)：扫描整个字符串并返回第一个成功的匹配，如果找到返回 Match 对象，否则返回 None。
#   - re.findall(pattern, string)：搜索字符串中所有与 pattern 相匹配的非重叠结果，⚠️ 并以列表的形式返回匹配结果。
#
# pattern = r'abc'，r 表示该字符串中的字符是原生字符串，即不会把字符串中 \n、\t 等进行转义。
#
# Match 对象常用方法：
#   - group()：返回匹配的字符串。
#   - start()：返回匹配开始的位置。
#   - end()：返回匹配结束的位置。
#   - span()：返回一个元组，包含匹配开始和结束的位置。


import re

s1 = "13345678901是我的第一个手机号，13345678902是我的第二个手机号。"
s2 = "我的第一个手机号是13345678901，13345678902是我的第二个手机号。"

match1 = re.match(r'1[3-9]\d{9}', s1) 
if match1:
    print("match 匹配结果：", match1.group()) 
else:
    print('match 匹配失败')


# ⚠️ 因为 s2 的开头不是手机号，所以 re.match 匹配失败。
match2 = re.match(r'1[3-9]\d{9}', s2) 
if match2:
    print("match2 匹配结果：", match2.group()) 
else:
    print('match2 匹配失败')


search1 = re.search(r'1[3-9]\d{9}', s2)
if search1:
    print("search 匹配结果：", search1.group())
else:
    print('search 匹配失败')

finall1 = re.findall(r'1[3-9]\d{9}', s2)
if finall1:
    print("findall 匹配结果：", finall1)  # ['13345678901', '13345678902']
else:
    print('findall 匹配失败')