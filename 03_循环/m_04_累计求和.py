"""
需求:
计算 0 ~ 100 之间所有数字的累计求和结果
"""
result = 0
i = 0
while i <= 100:
    result += i
    i += 1
print("0~100累计求和结果是%d" % result)
