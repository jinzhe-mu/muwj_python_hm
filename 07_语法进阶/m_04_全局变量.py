
# 全局变量 是在 函数外部定义 的变量，所有函数内部都可以使用这个变量
num = 10


def demo1():
    print("demo1调用全局变量 %d" % num)


def demo2():
    print("demo2调用全局变量 %d" % num)


demo1()
demo2()

