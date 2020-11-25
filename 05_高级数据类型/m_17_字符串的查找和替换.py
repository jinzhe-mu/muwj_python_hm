"""
2) 查找和替换 - 7
string.startswith(str)	                                检查字符串是否是以 str 开头，是则返回 True
string.endswith(str)	                                检查字符串是否是以 str 结束，是则返回 True
string.find(str, start=0, end=len(string))	            检测 str 是否包含在 string 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 -1
string.rfind(str, start=0, end=len(string))	            类似于 find()，不过是从右边开始查找
string.index(str, start=0, end=len(string))	            跟 find() 方法类似，不过如果 str 不在 string 会报错
string.rindex(str, start=0, end=len(string))	        类似于 index()，不过是从右边开始
string.replace(old_str, new_str, num=string.count(old))	把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次
"""

hello_str = "hello world"

# 1、判断是否以指定字符串开始
# string.startswith(str)
print(hello_str.startswith("he"))  # 返回True
print(hello_str.startswith("He"))  # 返回False

# 2、判断是否以指定字符串结束
# string.endswith(str)
print(hello_str.endswith("ld"))  # 返回True
print(hello_str.endswith("LD"))  # 返回False

# 3、查找指定字符串
# string.find(str, start=0, end=len(string))
# index 方法统一可以查找指定的字符在字符串中的索引
"""
区别：
> index方法如果指定的字符串不存在会报错
> find方法如果指定的字符串不存在，会返回-1
"""
print(hello_str.find("llo"))  # 存在>返回索引值
print(hello_str.find("abc"))  # 不存在>返回-1


# 4、替换字符串
# string.replace(old_str, new_str, num=string.count(old))
# replace 方法执行完成之后，会返回一个新的字符串
# 注意：但是不修改原有字符串的内容
print(hello_str.replace("world", "python"))  # 将修改后的字符串返回
print(hello_str)  # 不修改定义字符串的内容


