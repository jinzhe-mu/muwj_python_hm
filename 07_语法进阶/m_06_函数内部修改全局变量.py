# 全局变量
num = 10


def demo1():

    print("demo1" + "-" * 50)
    # 希望修改全局变量的值--使用global 声明一下变量即可
    # # global 关键字，告诉 Python 解释器 num 是一个全局变量
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建全局变量
    global num

    num = 99

    print("demo1调用全局变量 %d" % num)  # demo1调用全局变量 99


def demo2():
    print("demo2调用全局变量 %d" % num)  # demo2调用全局变量 99


demo1()
demo2()
