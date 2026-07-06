# 1、dict 字典的 “增” 操作
# 格式：字典名[key] = value
# 如果 key 存在，则更新其对应的 value；如果 key 不存在，则新增该 key-value 键值对。

d = {'name': '张三', 'age': 18}

d['sex'] = '男'
print('新增后的字典：', d)   # 新增后的字典： {'name': '张三', 'age': 18, 'sex': '男'}

d['name'] = '李四'
print('修改后的字典：', d)   # 修改后的字典： {'name': '李四', 'age': 18, 'sex': '男'}

# 1.2 update({})，批量新增多个元素
# 格式：字典名.update({key1: value1, key2: value2, ...})
d.update({'address': '北京市朝阳区', 'phone': '13912345678'})
print('批量新增后的字典：', d)   # 批量新增后的字典：  {'name': '李四', 'age': 18, 'sex': '男', 'address': '北京市朝阳区', 'phone': '13912345678'}

print("-------------------------------")

# 2、dict 字典的 “删” 操作

dict = {'name': '张三', 'age': 18, 'sex': '男'}

# 2.1 pop(key)，删除指定 key 的键值对，并返回该 key 对应的 value。如果 key 不存在，则报错 KeyError: 'xxx'
name = dict.pop('name')
print('删除的元素：', name)   # 删除的元素： 张三
print('删除后的字典：', dict)   # 删除后的字典： {'age': 18, 'sex': '男'}


# 2.1、del 字典名[key]
#   - 如果 key 存在，则删除该 key-value 键值对；
#   - 如果 key 不存在，则报错 KeyError: 'xxx'
del dict['age']
print('删除后的字典：', dict)   # 删除后的字典： {'sex': '男'}


print("-------------------------------")

# 3、dict 字典的 “改” 操作

dict = {'name': '张三', 'age': 18, 'sex': '男'}
# 直接赋值
dict['name'] = '李四'
print('修改后的字典：', dict)   # 修改后的字典： {'name': '李四', 'age': 18, 'sex': '男'}


print("-------------------------------")

# 4、dict 字典的 “查” 操作

dict = {'name': '张三', 'age': 18, 'sex': '男'}

# 4.1 通过 key 查找 value
print(dict['name'])   # 张三

print("---------------")

# 4.2 get(key)，返回指定 key 对应的 value，如果 key 不存在，则返回 None 或指定的默认值。
print(dict.get('name'))   # 张三
print(dict.get('address'))   # None
print(dict.get('address', '地址未知'))   # 地址未知

print("---------------")

# 4.3 keys()，返回一个可迭代对象，包含字典中所有的 key。
keys = dict.keys()
print(keys)   # dict_keys(['name', 'age', 'sex'])
for k in keys:
    print(k)

print("---------------")

# 4.4 values()，返回一个可迭代对象，包含字典中所有的 value。
values = dict.values()
print(values)   # dict_values(['张三', 18, '男'])
for v in values:
    print(v)

print("---------------")

# 4.5 items()，返回一个可迭代对象，包含字典中所有的 (key, value) 元组。
items = dict.items()
print(items)   # dict_items([('name', '张三'), ('age', 18), ('sex', '男')])
for item in items:
    print(item)
