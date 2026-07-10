# 1、定义类的实例方法
# 语法：
# class 类的名称:
#     def __init__(self, 参数1, 参数2, ...):
#         self.属性名 = 参数值
# 
#     # 实例方法定义：必须包含 self 作为第一个参数，用于访问类中的属性和其他方法。
#     def 方法名(self, 参数1, 参数2, ...):
#         # 方法体
#         pass
# 
# 实例方法：定义在类中的函数，用于操作对象的属性或执行某些任务。
# 注意：实例方法必须包含 self 作为第一个参数，用于访问类中的属性和其他方法。

class Car:
    def __init__(self, brand, color, price):  # 初始化方法，创建对象时自动调用
        self.brand = brand
        self.color = color
        self.price = price  
        print("Car 类型的对象初始化完毕！")

    def show_info(self):  
        """
        展示信息：品牌和颜色
        """
        print(f"品牌：{self.brand}, 颜色：{self.color}")

    # 计算总价
    def calculate_total(self, discount, rate = 0.1):
        """
        计算总价：原价 + 税率（原价 * 加价比例）
        :param discount: 折扣
        :param rate: 税率
        :return: 总价
        """
        return self.price * discount + self.price * rate
    

c3 = Car('宝马', '黑', 100000)
c3.show_info()  # 调用实例方法
price = c3.calculate_total(0.9, 0.1)
print(f"原价：{c3.price}, 总价：{price}")