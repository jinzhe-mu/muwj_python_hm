"""
如果字符串内部需要使用 "，可以使用 ' 定义字符串
如果字符串内部需要使用 '，可以使用 " 定义字符串
"""

str1 = "hello python"

str2 = "我的外号是'大西瓜'"
str3 = '我的外号是"大南瓜"'

print(str2)
print(str3)

print("根据索引从字符串中取小字符：", str1[9])

# 遍历字符串
for char in str1:
    print(char)

