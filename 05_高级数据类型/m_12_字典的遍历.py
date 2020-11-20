xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "gender": True,
                 "height": 180,
                 "weight": 140
                 }

# 迭代遍历字典
# key变量是每次循环中，获取到的键值对的key
for key in xiaoming_dict:

    # print(key)
    # print(xiaoming_dict[key])
    print("%s是 %s" % (key, xiaoming_dict[key]))
