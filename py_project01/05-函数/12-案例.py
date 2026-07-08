# 案例：电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息（如：商品名、价格、数量）、优惠信息（优惠券、积分抵扣）、运费信息来计算订单的总金额。
# 具体规则如下：
#   1、优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
#   2、积分抵扣需要商品金额满 5000 才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。

def calculate_order(*items, coupon=0, points=0, express_fee=10):
    """
    计算订单总金额
    :param items: 商品信息，列表形式，每个元素是一个字典，包含'name', 'price', 'quantity'
    :param coupon: 优惠券金额
    :param points: 积分
    :param express_fee: 运费
    """
    # 1、计算商品总金额
    # 方式1，for 循环
    # total_price = 0
    # for item in items:
    #     total_price += item[1] * item[2]

    # 方式2，⚠️ 列表推导式
    price_list = [good[1] * good[2] for good in items]
    total_price = sum(price_list)


    if total_price < 5000:
        return f"商品金额未达到使用优惠券和积分抵扣的最低标准，订单总价为：{total_price + express_fee}元。"

    # 2、使用优惠券
    if coupon > 0 and coupon <= total_price:
        total_price -= coupon
    else:
        coupon = 0

    # 3、使用积分抵扣
    if points >= 100:
        points_deduction = min(points // 100, int(total_price))
        total_price -= points_deduction
    else:
        points = 0
    
    # 4、添加运费
    total_price += express_fee

    # 5、返回结果
    return f"订单总价：{total_price}元，使用了{coupon}元的优惠券和{points}积分。"

# 测试代码1

print(calculate_order(('商品A',188,2),('商品B',388,1),('商品C',3999,1), coupon=10, points=4000, express_fee=9.9)) # 4772.9元。

print("--------------------\n")

# 测试代码2
print(calculate_order(('商品A',188,2),('商品B',388,1),('商品C',6999,1), coupon=10, points=4000, express_fee=9.9)) # 7722.9元