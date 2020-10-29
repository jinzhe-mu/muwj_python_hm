"""
可以用 其他变量的计算结果 来定义变量
变量定义之后，后续就可以直接使用了

需求:
苹果的价格是 8.5 元/斤
买了 7.5 斤 苹果
计算付款金额
加条件：
如果 只要买苹果，就返 5 块钱
请重新计算购买金额
"""
# 定义苹果的价格
apple_price = 8.5

# 定义购买苹果的重量
apple_weight = 7.5

# 计算购买苹果的金额
apple_money = apple_price * apple_weight
print("购买苹果的总价是：{}".format(apple_money))

# 当购买了苹果，价格优惠5块钱
if apple_money > 0:
    apple_money = apple_money - 5
    print("购买苹果有优惠，价格是：{}".format(apple_money))
else:
    print("没有购买苹果")
