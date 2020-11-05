"""
需求:
定义布尔型变量 has_ticket 表示是否有车票
定义整型变量 knife_length 表示刀的长度，单位：厘米
首先检查是否有车票，如果有，才允许进行 安检
安检时，需要检查刀的长度，判断是否超过 20 厘米
如果超过 20 厘米，提示刀的长度，不允许上车
如果不超过 20 厘米，安检通过
如果没有车票，不允许进门
"""
has_ticket = True

if has_ticket:
    print("车票验证通过，开始安检")
    print("有违禁用品")
    knife_length = int(input("刀的长度是："))
    if knife_length >= 20:
        print("刀的长度是%d，安检不通过" % knife_length)

    else:
        print("安检通过，祝您旅途愉快！")

else:
    print("您没有门票，不允许进站！")
