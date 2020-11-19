# 字典是一个无序的数据集合，使用print函数输出字典时，
# 通常数据的顺序和定义的顺序是不一致的！
# 为了美观，建议每个键值对独自占一行
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 180,
            "weight": 140
            }

print(xiaoming)
print(xiaoming.keys())  # 获取字典的键
print(xiaoming.values())  # 获取字典的值

# 转换成列表和元祖
print(list(xiaoming.keys()))
print(tuple(xiaoming.keys()))

