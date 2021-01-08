"""
需求

定义一个函数 sum_numbers
能够接收一个 num 的整数参数
计算 1 + 2 + ... num 的结果
"""


def sum_number(num):

    print(num)
    # 1、出口
    if num == 1:
        return 1

    # 2、数字的累加
    # 假设 sum_number 能够完成 num - 1 的累加
    tmp = sum_number(num-1)
    # 函数内部的核心算法就是 两个数字的相加
    return tmp+num


result_sum = sum_number(3)
print(result_sum)

