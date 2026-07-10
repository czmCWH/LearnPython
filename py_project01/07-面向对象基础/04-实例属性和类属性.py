# 1、实例属性
# 定义：实例属性属于每个具体对象的属性，每个对象都是独立的。(各个对象特有的数据)
# 访问：
#     对象名.属性名 

class Student:
    def __init__(self, name, age):
        # 实例属性，定义在__init__ 实例化方法中
        self.name = name  
        self.age = age

student1 = Student("小明", 20)
print(student1.name)  # 通过对象名访问实例属性

print("------------------------------\n")

# 2、类属性
# 定义：类属性是属于类本身的属性，所有实例共享的。(所有对象共享的数据或配置)
# 访问：
#     类名.属性名 
#
# ⚠️，获取属性值的顺序，通过对象名访问属性时，会先查找实例属性，如果没有找到，再查找类属性。

class Car:
    # 类属性，定义在类中但不在__init__方法内
    wheels_num = 4  # 轮胎数量
    tax_rate = 0.12  # 税率
    
    def __init__(self, brand):
        # 实例属性，定义在__init__方法内
        self.brand = brand  # 品牌
        self.tax_rate = 0.1  # 税率

# 2.1、所有对象访问类属性的值一样
print(Car.wheels_num)  # 4
c1 = Car("宝马")
print(c1.wheels_num)  # 4

c2 = Car("奔驰")
print(c2.wheels_num)  # 4

# 2.2、实例属性可以覆盖类属性的值
print(c1.tax_rate)  # 0.1
print(Car.tax_rate)  # 0.12
 