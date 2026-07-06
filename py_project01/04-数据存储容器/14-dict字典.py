# 1、dict 字典
# 概念：用于存储 key-value 键值对的可变数据结构，每一个 key 对应一个值，根据key来获取对应的 value.
# 特点；
#   1. 查询速度快；
#   2. 元素是无序的；
#   3. 元素的 key 必须是唯一的，value 可以重复。如果key重复定义，后面的会覆盖前面的；
#   4. key 必须是不可变类型，如：str、int、float、tuple，不能是 list、set、dict 等可变类型；
#   5. value 可以是任意类型，包括字符串、整数、列表、字典、集合等。 

dict = {'name': '张三', 'age': 18, 'sex': '男'}
print(type(dict))   # <class 'dict'>

print(dict['name'])   # 张三
dict['name'] = '李四'
print(dict['name'])   # 李四

# 定义空字典
d = {}
print(type(d))   # <class 'dict'>