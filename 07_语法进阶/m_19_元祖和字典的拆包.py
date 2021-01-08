"""
元组和字典的拆包（知道）
在调用带有多值参数的函数时，如果希望：

将一个 元组变量，直接传递给 args
将一个 字典变量，直接传递给 kwargs
就可以使用 拆包，简化参数的传递，拆包 的方式是：

在 元组变量前，增加 一个 *
在 字典变量前，增加 两个 *
"""


def demo(*args, **kwargs):

    print(args)
    print(kwargs)


#  元祖变量/字典变量
gl_nums = (1, 2, 6, 4)
gl_person = {"name": "小明", "age": 18}

# 会把 num_tuple 和 person 作为元组传递个 args
# demo(gl_nums, gl_person)
"""
结果：
((1, 2, 6, 4), {'name': '小明', 'age': 18})
{}
"""

# 当传入为字典或者元祖时，进行拆包，简化参数的传递
# 拆包语法，简化元祖变量/字典变量的传递
demo(*gl_nums, **gl_person)
"""
结果：
(1, 2, 6, 4)
{'name': '小明', 'age': 18}
"""