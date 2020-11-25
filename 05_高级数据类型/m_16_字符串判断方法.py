"""
方法	                    说明
1) 判断类型 - 9
string.isspace()	    如果 string 中只包含空格，则返回 True
string.isalnum()	    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True
string.isalpha()	    如果 string 至少有一个字符并且所有字符都是字母则返回 True
string.isdecimal()  	    如果 string 只包含数字则返回 True，全角数字
string.isdigit()	    如果 string 只包含数字则返回 True，全角数字、⑴、\u00b2
string.isnumeric()	    如果 string 只包含数字则返回 True，全角数字，汉字数字
string.istitle()	    如果 string 是标题化的(每个单词的首字母大写)则返回 True
string.islower()	    如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True
string.isupper()	    如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True
2) 查找和替换 - 7
string.startswith(str)	                                    检查字符串是否是以 str 开头，是则返回 True
string.endswith(str)	                                    检查字符串是否是以 str 结束，是则返回 True
string.find(str, start=0, end=len(string))	            检测 str 是否包含在 string 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 -1
string.rfind(str, start=0, end=len(string))	            类似于 find()，不过是从右边开始查找
string.index(str, start=0, end=len(string))	            跟 find() 方法类似，不过如果 str 不在 string 会报错
string.rindex(str, start=0, end=len(string))	            类似于 index()，不过是从右边开始
string.replace(old_str, new_str, num=string.count(old))	    把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次
3) 大小写转换 - 5
string.capitalize()	    把字符串的第一个字符大写
string.title()	            把字符串的每个单词首字母大写
string.lower()	            转换 string 中所有大写字符为小写
string.upper()	            转换 string 中的小写字母为大写
string.swapcase()	    翻转 string 中的大小写
4) 文本对齐 - 3
string.ljust(width)	            返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串
string.rjust(width)	            返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串
string.center(width)	            返回一个原字符串居中，并使用空格填充至长度 width 的新字符串
5) 去除空白字符 - 3
string.lstrip()	            截掉 string 左边（开始）的空白字符
string.rstrip()	            截掉 string 右边（末尾）的空白字符
string.strip()	            截掉 string 左右两边的空白字符
6) 拆分和连接 - 5
string.partition(str)	                把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
string.rpartition(str)	                类似于 partition() 方法，不过是从右边开始查找
string.split(str="", num)	        以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
string.splitlines()	                按照行('\r', '\n', '\r\n')分隔，返回一个包含各行作为元素的列表
string.join(seq)	                以 string 作为分隔符，将 seq 中所有的元素（的字符串表示）合并为一个新的字符串

"""
# 一、判断

# 1、判断空白字符  isspace 方法
# 字符串中只包含空格返回True
sapce1_str1 = " "
print(sapce1_str1.isspace())
# 字符串中包含空格及制表符以外的字符返回False
sapce1_str2 = "    a"
print(sapce1_str2.isspace())
# 字符串汇总只包含空格和制表符时返回True
sapce1_str3 = "    \t\n\r"
print(sapce1_str3.isspace())

print()

# 2、判断字符全是字字母或数字  isalnum  方法
# 字符串只包含字母返回True
sapce2_str1 = "abSCC"
print(sapce2_str1.isalnum())
# 字符串包含字母和数字返回True
sapce2_str2 = "23344sf"
print(sapce2_str2.isalnum())
# 字符串包含字母和数字以外的字符返回Flase
sapce2_str3 = "djj7d*"
print(sapce2_str3.isalnum())

print()

# 3、判断字符全部是字母  isalpha方法
# 字符串全是字母返回True
sapce3_str1 = "abSCC"
print(sapce3_str1.isalpha())
# 字符串包含字母以前的字符返回False
sapce3_str2 = "23344sf"
print(sapce3_str2.isalpha())
sapce3_str3 = "djj7d*"
print(sapce3_str3.isalpha())

print()

# 4、判断字符全部是全角数字 isdecimal 方法
"""
isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）
"""
# 字符串中只包含数字返回True

# 5、判断字符串只包含数字 全角数字、⑴、\u00b2  isdigit 方法
"""
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无
"""
# 6、判断只包含数字则返回 True，全角数字，汉字数字
"""
isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
"""

num_str1 = "三"  # 汉语数字
print(num_str1.isdigit())  # 返回False
print(num_str1.isdecimal())  # 返回False
print(num_str1.isnumeric())  # 返回True

print()

num_str2 = "1"  # unicode
print(num_str2.isdigit())  # 返回True
print(num_str2.isdecimal())  # 返回True
print(num_str2.isnumeric())  # 返回True

print()

num_str3 = "1"  # 全角
print(num_str3.isdigit())  # 返回True
print(num_str3.isdecimal())  # 返回True
print(num_str3.isnumeric())  # 返回True

print()

num_str4 = b"1"  # byte
print(num_str4.isdigit())  # 返回True
print(num_str4.isdecimal())  # 报错：AttributeError: 'bytes' object has no attribute 'isdecimal'
print(num_str4.isnumeric())  # 报错：AttributeError: 'bytes' object has no attribute 'isdecimal'

print()

num_str5 = "Ⅷ"  # 罗马数字
print(num_str5.isdigit())  # 返回False（理论上返回Ture）
print(num_str5.isdecimal())  # 返回False
print(num_str5.isnumeric())  # 返回Ture

print()


