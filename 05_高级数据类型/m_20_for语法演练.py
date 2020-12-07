"""
for 变量 in 集合:
    
    循环体代码
else:
    没有通过 break 退出循环，循环结束后，会执行的代码
"""
for num in [1, 2, 3]:
    print(num)

# 当 for循环没有加break，在for循环遍历完成后执行else下面的语句
else:
    print("会执行？")

print("结束！")
print()


for num1 in [1, 2, 3]:
    print(num1)
    if num1 == 2:
        break

# 当for循环加入了break，将不会执行else下面的语句
else:
    print("会执行吗？")

print("结束！")