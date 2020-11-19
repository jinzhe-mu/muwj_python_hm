info_tuple = ("小张", 21, 180)
info_list = [5, 8, "zhangsan"]

# 格式化字符串后面的 ‘()’ 本质上是元祖

print("%s 年龄是 %d 身高是 %.2f" % ("小明", 18, 185))

print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print("直接输出字符串：", info_str)

print()

# 元祖转列表 list(元祖)
print("元祖：", info_tuple)
print("元祖转列表：", list(info_tuple))

print()

# 列表转元祖 tuple(列表)
print("列表：", info_list)
print("列表转元祖：", tuple(info_list))

