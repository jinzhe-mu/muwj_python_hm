#  在 python 中，列表变量调用 += 本质上是在执行列表变量的 extend 方法，不会修改变量的引用
def demo(num, num_list):
    print("*" * 50)
    print("函数内部代码开始------------")  # 函数内部代码开始------------

    print("传入是实参", num_list)  # 传入是实参 [8, 9, 7]

    # 对数值来说，先算加法之后赋值，有赋值语句，函数内部变量将不会影响函数外部变量
    num += num
    print(num)  # 18

    # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    # += 操作本质上是执行extend操作，不等价num_list = num_list + num_list（此为一个赋值语句）
    num_list += num_list

    print("被修改后的参数", num_list)  # 被修改后的参数 [8, 9, 7, 1, 2, 6]

    print("函数内部代码执行完成--------")  # 函数内部代码执行完成--------


gl_num = 9
gl_list = [8, 9, 7]
demo(gl_num, gl_list)
print(gl_num)  # 9
print(gl_list)  # [8, 9, 7, 1, 2, 6]
print("*" * 50)