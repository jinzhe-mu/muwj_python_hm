xiaoming_dict = {"name": "小明",
                 "gender": True}

# 1、统计键值对数量
print("字典的长度：", len(xiaoming_dict))

# 2、合并字典
temp_dict = {"age": 18,
             "height": 175,
             "gender": False}

# 注意：如果被合并的字典中包含意见存在的键值对，会覆盖原有键值对
xiaoming_dict.update(temp_dict)
print("合并两个字典：", xiaoming_dict)

# 3\清空字典
xiaoming_dict.clear()


print("清空字典：", xiaoming_dict)
