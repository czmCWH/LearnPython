# dict 案例
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据通过控制台菜单与用户交互。具体功能如下:
#   1、添加购物车: 用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#   2、修改购物车: 要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#   3、删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#   4、查询购物车:将购物中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
#   4、退出系统: 退出系统，结束程序运行

# 1、定义购物车字典变量，用于存储购物车商品信息
menu = """
############## 购物车管理系统 ##############
1、添加购物车
2、修改购物车
3、删除购物车
4、查询购物车
5、退出系统
##########################################
"""
cart_dict = {}

print("欢迎使用购物车管理系统")
while True:
    
    print(menu)
    choice = input("请选择您需要执行的操作: ")
    match choice:
        case "1":
            name = input("请输入商品名称: ")
            price = float(input("请输入商品价格: "))
            count = int(input("请输入商品数量: "))
            if name in cart_dict:
                print("该商品已存在，无法重复添加。请重新选择操作")
            else:
                cart_dict[name] = {"price": price, "count": count}
                print(f"'{name}' 添加成功～")
        case "2":
            name = input("请输入要修改的商品名称: ")
            if name not in cart_dict:
                print(f"'{name}' 商品不存在。请重新选择操作")
                continue
            price = float(input("请输入商品最新价格: "))
            count = int(input("请输入商品最新数量: "))
            cart_dict[name]["price"] = price
            cart_dict[name]["count"] = count
            print(f"'{name}' 修改成功~")
        case "3":
            name = input("请输入要删除的商品名称: ")
            if name in cart_dict:
                del cart_dict[name]
                print(f"'{name}' 删除成功~")
            else:
                print(f"'{name}' 商品不存在。请重新选择操作")
        case "4": 
            for k, v in cart_dict.items():
                print(f"商品名称: {k}, 商品价格: {v['price']}, 商品数量: {v['count']}")
            else:
                print("购物车中商品获取完成～")
        case "5":
            print("退出系统成功，感谢您的使用")
            break
        case _:     # _，匹配其它所有情况
            print("非法操作，请重新选择操作")
