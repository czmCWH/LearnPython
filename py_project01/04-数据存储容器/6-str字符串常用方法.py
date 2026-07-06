# str 字符串常用方法
# ⚠️⚠️⚠️，str 字符串是不可变的，调用它的所有常用方法后，都会返回一个新的字符串，而不是修改原来的字符串。

# 1、find() 查找子串，返回第一个出现的索引，找不到返回 -1
s = 'hello world'
print(s.find('or'))       # 7
print(s.find('or', 0, 5)) # 查找索引 0~5 之间的字符串，-1

print("-------------------------------")

# 2、count() 统计子串出现的次数
print("count() = ", s.count('l'))    # 3
print("count() = ", s.count('l', 0, 5))   # 2

print("-------------------------------")

# 3、upper()、Lower()、swapcase() 大小写转换
s2 = 'Hello World'
print("字母全部大写", s2.upper())      # upper()，全部大写
print("字母全部大写：", s2.lower())    # lower()，全部小写
print("首字母大写，其他小写：", s.capitalize())    # capitalize() 首字母大写，其他全部大写小写

print("-------------------------------")

# 4、split() 分割字符串，返回一个列表
s3 = "hello world"
print(s3.split())   # 默认分割字符串为空格
print(s3.split('o'))   # 指定分割字符串
print(s3.split('o', 1))   # 指定分割次数为1次

print("-------------------------------")

# 5、strip() 去除两边的空格，或指定的字符串
s3 = "   人生苦短，我用Python "
ss = s3.strip()
print("去除2端空格 =", s3.strip())
s4 = "--人生苦短，我用Python--"
print("去除字符串两端指定的字符串 =", s4.strip("-"))

print("-------------------------------")

# 6、replace() 替换字符串
s5 = "hello Python"
print("替换字符串 =", s5.replace("Python", "Java"))
print("替换字符串 =", s5.replace("o", "*", 1))  # 替换次数为1次 

print("-------------------------------")

# 7、startswith()、endswith() 判断字符串是否以指定的字符串开头或结尾
s6 = "hello python"
print("是否以 hello 开头 =", s6.startswith("hello"))  # 返回 True
print("是否以 python 结尾 =", s6.endswith("python"))  # 返回 True
