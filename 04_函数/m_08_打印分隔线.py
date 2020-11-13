"""
需求 1:
定义一个 print_line 函数能够打印 * 组成的 一条分隔线

需求 2:
定义一个函数能够打印 由任意字符组成 的分隔线

需求 3:
定义一个函数能够打印 任意重复次数 的分隔线

需求 4:
定义一个函数能够打印 5 行 的分隔线，分隔线要求符合需求 3
"""


def print_line1():
    """直接打印"""
    print("*" * 50)


def print_line2(char2):
    """控制打印的次数"""
    print(char2 * 50)


def print_line3(char3, times3):
    """控制打印的字符，次数"""
    print(char3 * times3)


def print_line4(char4, times4, cow):
    """控制打印的字符，次数，行数"""
    col = 0
    while col < cow:
        print(char4 * times4)
        col += 1


print_line1()
print_line2("-")
print_line3("/", 20)
print_line4("mu", 10, 5)



