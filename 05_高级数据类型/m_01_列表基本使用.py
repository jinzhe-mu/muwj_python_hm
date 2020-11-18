name_list = ["zhangsan", "lisi", "wangwu", "lisi", "wangwu"]
print("列表原始值", name_list)

# 1、取值和取索引
#  list index out of range -列表索引超出范围
print("1.1 索引2的值：", name_list[2])  # 取值
print()

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不再列表中，程序会报错
print("1.2 wangwu的索引：", name_list.index("wangwu"))  # 取索引
print()


# 2、修改
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错
name_list[1] = "李四"

# 只能修改从索引0开始搜索到的第一个叫此名的元素
# 修改wangwu索引位置的元素
name_list[name_list.index("wangwu")] = "王五"
print("2.1 修改：", name_list)
print()


# 3、增加
# append 方法 在列表末位追加数据
name_list.append("maer")

# insert 方法 在列表指定索引位置插入元素
name_list.insert(2, "maer")

temp_list = ["孙悟空", "猪八戒", "沙师弟"]
# extend 方法 在当前列表末位加入另一个列表完整的内容
name_list.extend(temp_list)

print("3.1 增加：", name_list)
print()

# 4、删除
# 删除指定的字符,只能删除从索引0开始检测到的第一个叫此名字的元素
name_list.remove("maer")
print("4.1 remove maer：", name_list)
print()

# POP 方法可以指定要删除元素的索引
name_list.pop(1)
print("4.2 pop索引1：", name_list)
print()

# pop方法不带参数默认删除列表中最后一个元素
name_list.pop()
print("4.3 pop不带参数：", name_list)
print()


# clear 方法清空列表
name_list.clear()


print("clear后的结果：", name_list)

