"""
局部变量 是在 函数内部 定义的变量，只能在函数内部使用
局部变量的生命周期
所谓 生命周期 就是变量从 被创建 到 被系统回收 的过程
局部变量 在 函数执行时 才会被创建
函数执行结束后 局部变量 被系统回收
局部变量在生命周期 内，可以用来存储 函数内部临时使用到的数据
"""


def demo1():
    # 定义一个局部变量
    # 1>出生：执行了下方代码之后才会被创建
    # 2>死亡：函数执行完成之后，变量死亡
    num = 10
    print("在demo1函数内部的变量是 %d" % num)


"""
# num只能在demo1函数内使用，不能在demo1函数外进行使用
"""


def demo2():
    # print("%d" % num)  # NameError: name 'num' is not defined
    pass


# print("%d" % num)  # NameError: name 'num' is not defined

demo1()
demo2()

"""
局部变量 是在 函数内部 定义的变量，只能在函数内部使用
函数执行结束后，函数内部的局部变量，会被系统回收
不同的函数，可以定义相同的名字的局部变量，但是 彼此之间 不会产生影响
局部变量的作用：
在函数内部使用，临时 保存 函数内部需要使用的数据
"""


def demo3():
    # 创建一个局部变量
    num1 = 10
    print(num1)
    num1 = 20
    print("修改后 %d" % num1)


def demo4():

    num1 = 100
    print(num1)


demo3()
demo4()

print("over")


