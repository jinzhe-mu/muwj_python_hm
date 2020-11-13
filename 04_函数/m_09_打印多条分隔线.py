"""
需求 3:
定义一个函数能够打印 任意重复次数 的分隔线
需求 4:
定义一个函数能够打印 5 行 的分隔线，分隔线要求符合需求 3
"""


def print_line3(char3, times3):
    """控制打印的字符，次数"""
    print(char3 * times3)


def print_line4(cow):  # 控制打印的行数
    """调用需求3完成需求4"""
    col = 0
    while col < cow:
        print_line3("m", 50)
        col += 1


print_line4(5)
