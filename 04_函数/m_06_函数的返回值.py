def sum_2_num(num1, num2):
    """计算两个数字的求和"""
    # 注意：return 表示返回，后续的代码都不会被执行
    # return num1 + num2
    # print(f"{num1} + {num2} = {result}")

    result = num1 + num2

    # 使用返回值，告诉调用函数一方计算的结果
    return result


# 可以使用变量，来接受函数执行的返回结果
sum_result = sum_2_num(10, 20)
print(sum_result)
