"""
需求:
收银员输入 苹果的价格，单位：元／斤
收银员输入 用户购买苹果的重量，单位：斤
计算并且 输出 付款金额
"""
# 输入苹果的价格
apple_price_str = input("苹果的单价是：")  # input函数输入的数据类型是str的
apple_price = float(apple_price_str)  # 将苹果单价转换为浮点型
print(apple_price)

# 输入购买苹果的重量
apple_weight_str = input("苹果的重量是：")
apple_weight = float(apple_weight_str)  # 将苹果重量转换为浮点型
print(apple_weight)


# 计算购买苹果的金额
apple_money = apple_price * apple_weight
print("购买苹果的总价是：{}".format(apple_money))

# 当购买了苹果，且总价格大于5元,价格优惠5块钱
if 5 > apple_money > 0:
    print("购买苹果有优惠，价格是：{}".format(apple_money))
else:
    apple_money = apple_money - 5
    print("购买苹果有优惠，价格是：{}".format(apple_money))
