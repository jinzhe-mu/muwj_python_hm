"""
特点

一个函数 内部 调用自己

函数内部可以调用其他函数，当然在函数内部也可以调用自己
代码特点

函数内部的 代码 是相同的，只是针对 参数 不同，处理的结果不同

当 参数满足一个条件 时，函数不再执行

这个非常重要，通常被称为递归的出口，否则 会出现死循环！
"""


def sum_number(num):

    print(num)

    # 递归的出口，当函数满足某个条件时，不再执行函数
    if num == 1:
        return num

    # 自己调用自己
    sum_number(num-1)


result = sum_number(3)
print("result= %s " % result)