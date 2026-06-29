# 👉 1、type() 查看字面量/变量的数据类型
# 通过type()语句来得到数据的类型，具体语法为：type(要查看类型的数据)

# 查看字面量的数据类型
print(type("人生苦短，我用Python"))
print(type(10))
print(type(3.14))
print(type(True))
print(type(None))

print("-----------------")

# 查看变量的数据类型
# ⚠️ 变量是存储数据的容器，变量本身是没有类型的，type(变量)输出的类型是变量中存储的数据的类型
num = 0.5
print(type(num))

print("-----------------")

# 👉 2、 isinstance() 函数检查数据类型
# isinstance() 检查数据是否属于指定的类型，返回的是一个bool值，具体语法为：isinstance(数据，类型)
print(isinstance("人生苦短，我用Python", str))
print(isinstance(10, int))
print(isinstance(3.14, float))
print(isinstance(True, bool))
print(isinstance(None, type(None)))

print("--- num 是 int 类型吗？", isinstance(num, int))
print("--- num 是 float 类型吗？", isinstance(num, float))

print("-----------------")

# 👉 3、常见数据类型转换
#   - str() 函数将其他类型转换为字符串类型
#   - int() 函数将其他类型转换为整数类型
#   - float() 函数将其他类型转换为浮点数类型
#   - bool() 函数将其他类型转换为布尔类型
