"""
需求进阶:
计算 0 ~ 100 之间 所有 偶数 的累计求和结果
"""
result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
        print("i的值是=%d,result=%d" % (i, result))

    i += 1
    print("i的值是=%d" % i)

print("0~100偶数求和结果是%d" % result)
