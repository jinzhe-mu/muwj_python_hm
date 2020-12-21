"""
可变和不可变类型:

不可变类型，内存中的数据不允许被修改：
数字类型 int, bool, float, complex, long(2.x)
字符串 str
元组 tuple

可变类型，内存中的数据可以被修改：
列表 list
字典 dict
"""

# 1、列表
# 对列表使用方法修改数据，不会影响列表在内存中的地址
demo_list = [1, 2, 3]
print("demo_list是内存地址是:%d" % id(demo_list))  # demo_list是内存地址是:7942280

# 在变量demo_list后面追加内容（修改变量）
demo_list.append(66)
print(demo_list)  # [1, 2, 3, 66]
print("demo_list是内存地址是:%d" % id(demo_list))  # demo_list是内存地址是:7942280

demo_list.remove(2)
print(demo_list)  # [1, 3, 66]
print("demo_list是内存地址是:%d" % id(demo_list))  # demo_list是内存地址是:7942280

demo_list.clear()
print(demo_list)  # []
print("demo_list是内存地址是:%d" % id(demo_list))  # demo_list是内存地址是:7942280


# 对变量demo_list重新赋值
# 对列表使用赋值语句，会修改列表在内存中的地址
demo_list = []
print(demo_list)  # []
print("demo_list是内存地址是:%d" % id(demo_list))  # demo_list是内存地址是:8139304


# 2、字典
# 对字典使用方法修改数据，不会影响字典在内存中的地址
demo_dict = {"name": "xiaoming"}
print("demo_dict是内存地址是:%d" % id(demo_dict))  # demo_dict是内存地址是:7563856

demo_dict["age"] = 18  # 给字典d增加键值和内容
print(demo_dict)  # {'name': 'xiaoming', 'age': 18}
print("demo_dict是内存地址是:%d" % id(demo_dict))  # demo_dict是内存地址是:7563856

demo_dict.pop("age")  # 删除字典d中的"age"键值
print(demo_dict)  # {'name': 'xiaoming'}
print("demo_dict是内存地址是:%d" % id(demo_dict))  # demo_dict是内存地址是:7563856

# 给字典demo_dict重新赋值
# 对字典使用赋值语句，会修改字典在内存中的地址
demo_dict = {"name": "xiaohong",
     "age": 18}
print(demo_dict)  # {'name': 'xiaohong', 'age': 18}
print("demo_dict是内存地址是:%d" % id(demo_dict))  # demo_dict是内存地址是:7564216


