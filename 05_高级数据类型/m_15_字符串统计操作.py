"""字符串方法：
In [1]: hello_str.
hello_str.capitalize    hello_str.isidentifier  hello_str.rindex
hello_str.casefold      hello_str.islower       hello_str.rjust
hello_str.center        hello_str.isnumeric     hello_str.rpartition
hello_str.count         hello_str.isprintable   hello_str.rsplit
hello_str.encode        hello_str.isspace       hello_str.rstrip
hello_str.endswith      hello_str.istitle       hello_str.split
hello_str.expandtabs    hello_str.isupper       hello_str.splitlines
hello_str.find          hello_str.join          hello_str.startswith
hello_str.format        hello_str.ljust         hello_str.strip
hello_str.format_map    hello_str.lower         hello_str.swapcase
hello_str.index         hello_str.lstrip        hello_str.title
hello_str.isalnum       hello_str.maketrans     hello_str.translate
hello_str.isalpha       hello_str.partition     hello_str.upper
hello_str.isdecimal     hello_str.replace       hello_str.zfill
hello_str.isdigit       hello_str.rfind
"""

str1 = "hello python"

# 1、统计字符串长度
print(len(str1))

# 2、统计某一个小（子）字符串出现的次数
# 如果使用count方法查找的子字符串不存在，不会报错，计数为0
print(str1.count("llo"))
print(str1.count("lbnv"))

# 3、某一个字符串出现的位置
print("子字符串出现的索引位置：", str1.index("llo"))
# 注意：如果使用index方法传递的子字符串不存在，程序会报错！
# print(str1.index("abc"))
