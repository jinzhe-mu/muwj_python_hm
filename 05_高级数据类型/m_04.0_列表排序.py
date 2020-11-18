num_list = [2, 5, 9, 22, 1, 98, 25]
name_list = ["zhangsan", "lisi", "wangwu", "wanxiaoer"]
num_list1 = [2, 5, 9, 22, 1, 98, 25]
name_list1 = ["zhangsan", "lisi", "wangwu", "wanxiaoer"]
print(num_list)
print(name_list)
print()

# 升序
num_list.sort()
name_list.sort()

print("升序排序：", num_list)
print("升序排序：", name_list)
print()

# 降序
num_list.sort(reverse=True)

print("降序排序：", num_list)
print("降序排序：", name_list)
print()


# 逆序（反转）

num_list1.reverse()
name_list1.reverse()

print("逆序排序：", num_list1)
print("逆序排序：", name_list1)


