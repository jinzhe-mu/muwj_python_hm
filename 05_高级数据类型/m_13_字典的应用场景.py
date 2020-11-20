"""
尽管可以使用 for in 遍历 字典

但是在开发中，更多的应用场景是：

* 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
* 将 多个字典 放在 一个列表 中，再进行遍历，在循环体内部针对每一个字典进行 相同的处理
"""

card_list = [{"name": "小明",
              "qq": 123456,
              "phone": 15896324564},
             {"name": "小画",
              "qq": 456789,
              "phone": 15896324569}
             ]
cow = 1

# 先遍历列表
for card_personal in card_list:
    # print(personal)
    print(f"第{cow}个人信息：")
    cow += 1
    # 遍历列表里的字典
    for information_dict in card_personal:
        print("%s : %s" % (information_dict, card_personal[information_dict]))


