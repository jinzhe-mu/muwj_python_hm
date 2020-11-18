name_list = ["李四", "张三", "王五", "王小二", "张三"]

# len（length 长度）函数可以统计列表汇总元素的总数（列表长度）
list_len = len(name_list)

# 三种输出方式
print("列表中包含 {} 个元素".format(list_len))
print(f"列表中包含 {list_len} 个元素")
print("列表中包含 %d 个元素" % list_len)


# count 方法可以统计列表中某一个元素出现的次数
list_count = name_list.count("张三")
print(f"张三出现了{list_count}次")

# 从列表中删除元素(删除第一次出现的元素）
# 如果数据不存在，程序会报错
print(name_list)
name_list.remove("张三")

print(name_list)

