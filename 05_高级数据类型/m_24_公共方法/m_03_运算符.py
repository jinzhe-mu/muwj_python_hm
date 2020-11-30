"""
运算符	            Python表达式	                    结果	                描述	            支持的数据类型
+	            [1, 2] + [3, 4]	              [1, 2, 3, 4]	        合并	            字符串、列表、元组
*	            ["Hi!"] * 4	           ['Hi!', 'Hi!', 'Hi!', 'Hi!']	        重复	        字符串、列表、元组
in	            3 in (1, 2, 3)	            True	                元素是否存在	    字符串、列表、元组、字典
not in	        4 not in (1, 2, 3)	            True	            元素是否不存在	 字符串、列表、元组、字典
> >= == < <=	(1, 2, 3) < (2, 2, 3)	            True	            元素比较	            字符串、列表、元组
注意

in 在对 字典 操作时，判断的是 字典的键
in 和 not in 被称为 成员运算符
"""
# + (合并)
t_list = [1, 2]
print([1, 2] + [3, 4])  # 结果:[1, 2, 3, 4] 列表

# extend方法 与 append的区别
t_list.extend([1, 5])
print(t_list)  # 结果 [1, 2, 1, 5]
t_list.append(9)  # 结果 [1, 2, 1, 5, 9]
print(t_list)
t_list.append([8, 9])  # 结果 [1, 2, 1, 5, 9, [8, 9]]
print(t_list)

# 元组
print((1, 2) + (3, 4))  # 结果：(1, 2, 3, 4)

# 字符
print("123"+"569")  # 结果：123569


# *(重复)
# 列表
print(["Hi!"] * 4)  # 结果：['Hi!', 'Hi!', 'Hi!', 'Hi!']
# 元组
print((1, 2) * 4)  # 结果：(1, 2, 1, 2, 1, 2, 1, 2)
# 字符
print("12"*4)  # 结果：12121212

# print({"a": 3, "b": 5, "c": 6}+{"d": 3, "e": 5, "c": 6})
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'



