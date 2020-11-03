apple = 1
banana = 2
pear = 3
apple_money = 0
banana_money = 0
pear_money = 0
while True:
    fruits = float(input("购买的水果是："))
    if fruits == 1:
        # apple_price = float(input("苹果的价格是："))
        apple_price = 7.5
        apple_weight = float(input("苹果的重量是："))
        apple_money = apple_price * apple_weight
        if 5 > apple_money > 0:
            print("苹果的价格是：{}".format(apple_money))
        else:
            apple_money = apple_money-5
            print("苹果{}一斤".format(apple_price), "苹果总价是：{}".format(apple_money))

    elif fruits == 2:
        # banana_price = float(input("香蕉的价格是："))
        banana_price = 5
        banana_weight = float(input("香蕉的重量是："))
        banana_money = banana_price * banana_weight
        print("香蕉{}一斤".format(apple_price), "香蕉总价是：{}".format(banana_money))

    elif fruits == 3:
        # pear_price = float(input("梨的价格是："))
        pear_price = 6
        pear_weight = float(input("梨的重量是："))
        pear_money = pear_price * pear_weight
        print("梨{}一斤".format(pear_price), "梨总价是：{}".format(pear_money))

    elif fruits == 000:
        break
    else:
        print("请输入正确商品编码")

money = apple_money + banana_money + pear_money
print("水果总价是：{}".format(money))
