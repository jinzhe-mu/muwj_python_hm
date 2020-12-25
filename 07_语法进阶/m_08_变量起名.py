"""
全局变量命名的建议
为了避免局部变量和全局变量出现混淆，在定义全局变量时，有些公司会有一些开发要求，例如：
全局变量名前应该增加 g_ 或者 gl_ 的前缀
提示：具体的要求格式，各公司要求可能会有些差异
"""

gl_num = 10
# 再定义一个全局变量
gl_title = "黑马程序员"
#  再定义一个全局变量
gl_name = "小米"


def demo():

    # 如果局部变量的名字和全局变量名字相同
    # pycharm会在局部变量下发显示一个虚线
    # 提示和全局变量名字相同了
    num = 99

    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)

