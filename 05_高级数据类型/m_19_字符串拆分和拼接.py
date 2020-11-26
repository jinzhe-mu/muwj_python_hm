"""
6) 拆分和连接 - 5
string.partition(str)	        把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
string.rpartition(str)	        类似于 partition() 方法，不过是从右边开始查找
string.split(str="", num)	    以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
string.splitlines()	            按照行('\r', '\n', '\r\n')分隔，返回一个包含各行作为元素的列表
string.join(seq)	            以 string 作为分隔符，将 seq 中所有的元素（的字符串表示）合并为一个新的字符串
"""
# 要求：
# 2、将字符串中的空白字符全部去掉
# 2、再使用""作为分隔符，拼接成一个整齐的字符串
poem_str = " 登鹳雀楼 \t\t\n   王之涣  \t 白日依山尽 \t\n 黄河入海流 \t 欲穷千里目 \t 更上一层楼"

print(poem_str)

# 1、拆分字符串
poem_list = poem_str.split()
print("拆分字符串：", poem_list)
# 结果：['登鹳雀楼', '王之涣', '白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']

# 2、合并字符串(以列表合并成字符串）
result = " ".join(poem_list)
print("合并字符串：", result)
# 结果：登鹳雀楼 王之涣 白日依山尽 黄河入海流 欲穷千里目 更上一层楼

poem_str2 = "abhchhhhkh降级感觉刚好"

# 3、字符串拆分成3个元素构成的元祖（左边开始查找）
print(poem_str2.partition("h"))  # 以h为分割拆分，从左边查找
# 结果：('ab', 'h', 'chhhhkh降级感觉刚好')

# 4、字符串拆分成3个元素构成的元祖（右边开始查找）
print(poem_str2.rpartition("h"))  # 以h为分割拆分，从右边查找
# 结果：('abhchhhhk', 'h', '降级感觉刚好')

# 5、按照行('\r', '\n', '\r\n')分隔，返回一个包含各行作为元素的列表

poem_str3 = " 登鹳雀楼 \n   王之涣  \r 白日依山尽 \r\n 黄河入海流 \n 欲穷千里目 \r 更上一层楼"

print(poem_str3.splitlines())
# 结果：[' 登鹳雀楼 ', '   王之涣  ', ' 白日依山尽 ', ' 黄河入海流 ', ' 欲穷千里目 ', ' 更上一层楼']
