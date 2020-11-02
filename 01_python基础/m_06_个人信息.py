"""
定义变量保存小明的个人信息
姓名：小米
年龄：18 岁
性别：是男生
身高：1.75 米
体重：75.0 公斤
"""
# 单步调试查看数据类型
name = '小米'  # str 表示是一个字符串类型
age = 18  # int 表示是一个整数类型
gender = True  # bool 表示是一个布尔值（真：True或假：False）
height = 1.75  # float 标识是一个浮点型
weight = 75
# 在python中，，定义变量是不需要制定变量的类型的
# 在运行的时候，python解释器，会更加复制语句等号右侧的数据
# 自动推导出变量中保存数据的准确类型
print(type(name))  # 直接输出数据类型的方式
print(type(age))
print(type(gender))
print(type(height))
print(type(weight))
