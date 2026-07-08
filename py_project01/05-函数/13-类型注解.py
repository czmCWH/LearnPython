# 1、类型注解
# 定义：类型注解（Type Hints）是 Python 3.5+ 新增的特性，也叫类型提示，用于给变量、函数参数和返回值指定类型。

# 定义变量
a: int = 10
score: float = 98.5
hobby: str = "coding"
flag: bool = True
pic: None = None

names: list[str] = ["Tom", "Jerry"]
goods: tuple[str, int] = ("apple", 10)
phones: set[str] = {"123456", "654321"}
ages: dict[str, int] = {"Tom": 18, "Jerry": 20}

# 如果类型注解需要多个类型，可以使用 ｜
value: int | str = 10

# 2、类型注解的好处
# 提高代码的可读性：通过类型注解，其他开发者可以更容易地理解你的代码意图。
# 提供更好的错误信息：在开发过程中，如果使用了类型注解并且发生了类型不符的情况

# 3、类型注解只起到提示作用，不强制执行类型检查。
# Python 是动态类型的语言，这意味着你可以在任何时候改变变量的类型。使用类型注解只是添加提示，Python 不会强制执行这些类型检查。
# 但是，你可以使用一些工具（如 mypy）来静态地分析你的代码并找出潜在的错误。

# 4、类型推断
# 类型推断（Type Inference）是 Python 的一个特性，Python 解释器自动推断出变量、表达式或函数返回值的数据类型的能力，而无需开发者显式指定。
# 当你定义一个变量而没有指定类型时，Python 会根据变量的值自动推断出它的类型。鼠标移动到变量上，可以看到变量的类型。
d = 10
print(type(d))  # <class 'int'>
str = "hello"
tag = True
list = [1, 2, 3]

# 注意，在对变量进行直接赋值，或者涉及到变量的运算、容器的推导等场景时，Python 会自动推断出变量的类型。


# 5、函数的类型注解
# 定义：在函数定义时，可以使用类型注解来指定 参数 和 返回值 的类型。
# 语法：
#     def 函数名(参数名: 类型) -> 返回值类型:

# 5.1、参数类型注解
def greet(name: str) -> None:
    print("Hello, " + name)

# 5.2、返回值类型注解
def add(x: int, y: int) -> int:
    return x + y

# 使用类型注解的函数，在调用时如果不符合预期的类型，Python 会抛出 TypeError。
greet("Tom")  # Hello, Tom
total = add(10, 20)  
print(total)  # 30

print("-----------------------------")

def circle_calc(r: float) -> tuple[float, float]:
    """
    计算圆的周长和面积，返回一个元组。
    """
    c = round(2 * 3.14 * r, 2)  # 保留两位小数
    s = round(3.14 * r**2, 2)   # 保留两位小数
    return c, s

result = circle_calc(5)
print(f"半径为5的圆的周长: {result[0]}, 面积为: {result[1]}")


# 为不定长参数的函数，添加类型注解
def sum_numbers(*args: int) -> int:
    return sum(args)

print(sum_numbers(1, 2, 3))  # 6

"""
总结：
对于需要团队协作开发和长期维护的项目，推荐使用类型注解。
"""