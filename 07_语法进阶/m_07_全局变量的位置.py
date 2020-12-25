#  注意：在开发时，应该吧模块中的所有局部变量
#  定义在所有函数上方，就可以保证所有的函数
#  都可以正常的访问到每一个全局变量
num = 10
# 再定义一个全局变量
title = "黑马程序员"
#  再定义一个全局变量
name = "小米"


def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


# 再定义一个全局变量
# title = "黑马程序员"
# 此时还可以正常调用
demo()

#  再定义一个全局变量
# name = "小米"
#  如果定义在这，此时程序报错没有定义变量name
#  NameError: name 'name' is not defined
