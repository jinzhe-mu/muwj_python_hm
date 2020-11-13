def test1():
    print("*" * 50)
    print("test1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test2")

    test1()  # 在函数test2中调用test1，观察执行顺序
    print("-" * 50)


test2()
