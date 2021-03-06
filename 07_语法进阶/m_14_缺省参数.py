"""
定义函数时，可以给 某个参数 指定一个默认值，具有默认值的参数就叫做 缺省参数
调用函数时，如果没有传入 缺省参数 的值，则在函数内部使用定义函数时指定的 参数默认值
函数的缺省参数，将常见的值设置为参数的缺省值，从而 简化函数的调用
"""

gl_list = [9, 5, 8, 2, 1]

# sort（）方法中应该跟随一个参数，但是有默认值为升序排序，可以省略
# 既为sort（）方法的缺省参数，缺省参数是reverse，默认值是False
# 默认就是升序排序，因为这种应用需求更多
gl_list.sort()
print(gl_list)

# 只有当需要降序排序时，才需要传递 `reverse` 参数
gl_list.sort(reverse=True)
print(gl_list)


