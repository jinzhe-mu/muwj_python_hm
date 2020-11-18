"""
使用 del 关键字(delete) 同样可以删除列表中元素
del 关键字本质上是用来 将一个变量从内存中删除的
如果使用 del 关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
del name_list[1]
"""
name_list = ["张三", "李四", "王五"]

# （知道）只用del 关键字（delete）删除里边元素
# 提示： 在日常开发中，要从列表删除数据，建议使用列表提供的方法，建议不要用del
del name_list[1]

# del 关键字的本质上是将一个变量从内存中删除
name = "小明"

del name

# 注意使用del关键字将变量从内从中删除
# 后续的代码就不能再使用这个变量了
print(name)
# 此时输出报错： name 'name' is not defined（因为name已经被从内存中删除）

print(name_list)
