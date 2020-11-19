# 定义元祖变量
info_tuple = ("zhangsan", 18, 175, "zhangsan", 18)

print(info_tuple)
print(info_tuple[0])  # 元祖的单个元素输出和列表一致，用索引


# 空元祖定义（一般很少使用，因为元祖定义后就没有办法修改）
empty_tuple = ()

print(type(empty_tuple))


#  定义单个元祖的方式，单个元素后面加逗号
single_tuple = (5,)
print(type(single_tuple))

# 1、取值和取索引
# index 方法
print("取出索引是1的元祖值：", info_tuple[1])
# 已经知道数据的内容，希望知道该数据在元祖中的索引
# 只能取出第一个为18的元素的索引值
print("取数元祖中元素为18的索引值：", info_tuple.index(18))

# 2、统计计数
# count 方法
print("此元素在元祖中出现的次数：", info_tuple.count("zhangsan"))
# 统计元祖中包含元素的个数
print("元祖的长度", len(info_tuple))


