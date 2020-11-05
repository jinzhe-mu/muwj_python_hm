"""
定义 holiday_name 字符串变量记录节日名称
如果是 情人节 应该 买玫瑰／看电影
如果是 平安夜 应该 买苹果／吃大餐
如果是 生日 应该 买蛋糕
其他的日子每天都是节日啊……
"""
holiday_name = input("今天的节日是：")

if holiday_name == "情人节":
    print("今天是%s，应该买玫瑰和看电影" % holiday_name)

elif holiday_name == "平安夜":
    print("今天是%s，应该买苹果和吃大餐" % holiday_name)

elif holiday_name == "生日":
    print("今天是%s，应该买蛋糕" % holiday_name)
else:
    print("每天都是节日啊")

