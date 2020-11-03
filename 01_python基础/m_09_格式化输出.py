# 定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
name = "小明"
print("我的名字叫%s,请多多关照！" % name)

# 定义整数变量 student_no，输出 我的学号是 000001
student_no = 1
print("我的学号是：%06d" % student_no)

# 定义小数 price、weight、money，输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
price = 9
weight = 5
money = price * weight
print("苹果单价%.2f/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.1
print("数据比例是%.2f%%" % (scale * 100))

"""
格式化字符	含义
%s	        字符串
%d	        有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用 0 补全
%f	        浮点数，%.2f 表示小数点后只显示两位
%%	        输出 %
"""
