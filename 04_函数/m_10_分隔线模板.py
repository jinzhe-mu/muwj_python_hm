"""
需求 3:
定义一个函数能够打印 任意重复次数 的分隔线
需求 4:
定义一个函数能够打印 5 行 的分隔线，分隔线要求符合需求 3
"""


def print_line3(char, times):
    """控制打印的字符，次数"""
    print(char * times)


def print_line4(char, times, cow):  # cow控制打印的行数
    """通过调用需求3完成需求4打印分隔线

    :param char: 分隔线使用的风格字符
    :param times: 分隔线重复的次数
    :param cow: 分隔线的行数
    """
    #  光标停留在函数上，等待一下出现黄色小灯泡，选择“Add Type..."选择，可以自动增加对参数解释的注释
    col = 0
    while col < cow:
        print_line3(char, times)
        col += 1


print_line4("2", 20, 5)  # 选择函数后按ctrl+Q可以查看对函数的注释
