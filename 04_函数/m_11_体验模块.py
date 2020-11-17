"""
模块名也是一个标识符
标示符可以由 字母、下划线 和 数字 组成
不能以数字开头
不能与关键字重名
注意：如果在给 Python 文件起名时，以数字开头 是无法在 PyCharm 中通过导入这个模块的
"""
import m_10_分隔线模板


def modular():
    print(m_10_分隔线模板.name)
    m_10_分隔线模板.print_lines("*", 5, 1)
    print(m_10_分隔线模板.name)


modular()


