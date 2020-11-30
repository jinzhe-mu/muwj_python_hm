"""
in	            3 in (1, 2, 3)	            True	                元素是否存在	    字符串、列表、元组、字典
not in	        4 not in (1, 2, 3)	            True	            元素是否不存在	 字符串、列表、元组、字典
> >= == < <=	(1, 2, 3) < (2, 2, 3)	            True	            元素比较	            字符串、列表、元组
注意

in 在对 字典 操作时，判断的是 字典的键
in 和 not in 被称为 成员运算符
"""
# in \ not in  (元素是否存在 \ 元素是否不存在)
# 列表
print(3 in [1, 2, 3])  # 结果：True
print(3 not in [1, 2, 3])  # 结果：False
# 元组
print(4 in (1, 2, 3))  # 结果：False
print(4 not in (1, 2, 3))  # 结果：True
# 字符
print("5" in "123456")  # 结果：True
print("5" not in "123456")  # 结果：False
# 字典
print("a" in {"a": 3, "b": 5, "c": 6})  # 结果：True
print("a" not in {"a": 3, "b": 5, "c": 6})  # 结果：False

# > >= == < <= (元素比较)

print([1, 2, 3] > [2, 1, 3])  # 结果：False

print((1, 2, 3) < (2, 1, 3))  # 结果：True

print("123" >= "213")  # 结果：False
