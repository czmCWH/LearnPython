# 1、魔法方法
# 魔法方法是指 Python 中一些特殊的方法，它们以双下划线开头和结尾（例如 __init__、__str__ 等）。
# 作用：魔法方法用于定义类的特殊行为，例如初始化、字符串表示等。
#
# ⚠️，魔法方法无需手动调用，Python 会在特定情况下自动调用它们。
# 
# 常见的魔法方法：
# __init__：类的初始化方法，用于创建对象时进行初始化操作。
# __str__：返回对象的字符串表示形式，常用于打印对象时的输出。
# __eq__：比较2个对象是否相等。
# __lt__, __gt__, __le__, __ge__: 分别定义了小于、大于、小于等于、大于等于的比较行为。
# __repr__：返回对象的官方（正式）字符串表示形式，主要用于调试和日志记录等场景。
# __add__、__sub__ 等：定义了算术运算符的行为，例如加法（+）、减法（-）。

class Person:
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return f"姓名：{self.name}, 年龄：{self.age}, 性别：{self.gender}"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.score == other.score
        else:
            return False
    

p1 = Person("小明", 20, "男", 90)
# ⚠️ 使用 __str__ 方法输出对象信息
print(p1)  

p2 = Person("小红", 22, "女", 85)
# ⚠️ 使用 __eq__ 方法比较对象的属性值（分数）
is_equal = p1 == p2
print(f"{p1.name} 和 {p2.name} 的分数是否相同？{'是' if is_equal else '否'}")
