"""
4) 文本对齐 - 3
string.ljust(width)	            返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串
string.rjust(width)	            返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串
string.center(width)	        返回一个原字符串居中，并使用空格填充至长度 width 的新字符串
"""
# 要求：顺序并且居中对齐输出以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

poem2 = [" 登鹳 雀楼 \t\n",
         " \t\n   王之涣  ",
         "   白日依山尽 ",
         " 黄河入海流 ",
         " 欲穷千里目 ",
         " 更上一层楼 "]
# i = 0
# while i < len(poem):
#     print(poem[i].center(10))
#     i += 1
for poem_str in poem:
    # 用方法对齐是默认是用英文的空格
    # 当英文空格不能达到要求时，切换为中文半角状态下，加入空格参数
    print("|%s|" % poem_str.center(10, "　"))

for poem_str in poem:
    # 用方法对齐是默认是用英文的空格
    # 当英文空格不能达到要求时，切换为中文半角状态下，加入空格参数
    print("|%s|" % poem_str.ljust(10, "　"))

for poem_str in poem:
    # 用方法对齐是默认是用英文的空格
    # 当英文空格不能达到要求时，切换为中文半角状态下，加入空格参数
    print("|%s|" % poem_str.rjust(10, "　"))


# 2、字符串去除空白字符

# 先使用strip方法去除字符串中的空白字符
# 再使用center方法使字符串居中显示文本
for poem_str2 in poem2:
    print("|%s|" % poem_str2.strip().center(10, "　"))
