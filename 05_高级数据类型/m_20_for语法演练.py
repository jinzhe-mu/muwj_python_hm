"""
for 变量 in 集合:
    
    循环体代码
else:
    没有通过 break 退出循环，循环结束后，会执行的代码
"""
"""
应用场景
在 迭代遍历 嵌套的数据类型时，例如 一个列表包含了多个字典
需求：要判断 某一个字典中 是否存在 指定的 值 
如果 存在，提示并且退出循环
如果 不存在，在 循环整体结束 后，希望 得到一个统一的提示
"""
# students = [{"name": "小金", "eag": 18, "gender": True, "weight": 56, "height": 160},
#                 {"name": "小名", "eag": 19, "gender": False, "weight": 62, "height": 180},
#                 {"name": "小雪", "eag": 17, "gender": True, "weight": 50, "height": 156},
#                 {"name": "小沐", "eag": 16, "gender": True, "weight": 52, "height": 171},
#                 {"name": "小李", "eag": 20, "gender": False, "weight": 63, "height": 183}
#                 ]
#
# find_name = input("请输入查找人姓名：")
#
# for stu_dict in students:
#     print(stu_dict)
#     # 判断当前遍历的字典中姓名是否为find_name
#     if stu_dict["name"] == find_name:
#         print("找到了")
#         # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
#         break
# else:
#     print("没有找到")
# print("循环结束")


student_list = [{"name": "小金", "eag": 18, "gender": True, "weight": 56, "height": 160},
                {"name": "小名", "eag": 19, "gender": False, "weight": 62, "height": 180},
                {"name": "小雪", "eag": 17, "gender": True, "weight": 50, "height": 156},
                {"name": "小沐", "eag": 16, "gender": True, "weight": 52, "height": 171},
                {"name": "小李", "eag": 20, "gender": False, "weight": 63, "height": 183}
                ]


def finds():
    print()
    find_name = input("请输入查找人姓名：")
    # 循环所有字典进行查找
    for student_dic in student_list:

        # 判断当循环到的name键值是否等于等于find_name
        if student_dic["name"] == find_name:
            # 如果等于，将字典的信息以字符串的方式输出
            for student_str in student_dic:
                print(f"{student_str}是：{student_dic[student_str]}", end=" \t")
    # 如果查询不到，输出 查无此人！
    else:
        """
        else搭配for循环进行使用
        """
        print("查无此人！")
        print()


while True:

    find_choice = input("是否查找学生信息N/Y：")
    # 如果为Y，查找学生信息
    if find_choice == "Y":
        finds()
    elif find_choice == "N":
        print()
        print("退出查找！")
        break
    else:
        print()
        print("请输入N/Y进行查找！")
        print()





