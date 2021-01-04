def measure():
    """测量温度和湿度"""
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元祖-可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # return (temp, wetness)
    return temp, wetness


# 元祖
result = measure()
print(result)

# 需要单独的处理温度或湿度。。不方便
print(result[0])
print(result[1])

# 如果开发中一个函数返回的类型是元祖，同时希望单独的处理元祖中的元素
# 可以使用多个变量，一次性接受函数中的返回值
# 注意：使用多个变量接受结果时，变量的个数应该和元祖的中的元素数量保持一致
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)




