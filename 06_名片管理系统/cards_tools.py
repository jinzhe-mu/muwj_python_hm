card_list = []


# 显示菜单
def show_menu():
    """
    显示菜单
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


# 新建名片
def new_menu():
    """
        新建名片
        """
    print("*" * 50)
    print("功能：新建用户名片")

    # 1. 提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input("请输入手机：")
    qq = input("请输入QQ号：")
    email = input("请输入邮箱：")
    # 2. 将用户信息保存到一个字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email
                 }

    # 3. 将用户字典添加到名片列表
    card_list.append(card_dict)
    print(card_dict)

    # 4. 提示添加成功信息
    print(f"已成功添加 “{card_dict['name']}” 的名片")


# 显示全部名片
def show_all():
    """
    显示全部名片
    """
    print("*" * 50)
    print("功能：搜索名片")

    # 1. 判断是否有名片记录
    if len(card_list) == 0:
        print("提示：没有任何名片记录")
        return

    # 2.如果有记录，进行查找遍历
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t\t")
    print()
    print("-" * 50)

    for card_dic in card_list:

        for card_str in card_dic:
            print(f"{card_dic[card_str]}", end="\t\t\t")

        print()


# 搜索名片
def search_card():
    """
    搜索名片
    """
    print("*" * 50)
    print("功能：搜索名片")

    while True:

        find_choice = input("是否继续查找学生信息N/Y：")
        # 如果为Y，查找学生信息
        if find_choice == "Y":
            # 调用查找函数
            finds()
        elif find_choice == "N":
            print()
            print("退出查找！")
            break
        else:
            print()
            print("请输入N/Y进行查找！")
            print()


# 查找名片
def finds():
    """
    查找名片
    :return:
    """
    print()
    find_name = input("请输入查找人姓名：")
    # 循环所有字典进行查找
    for card_dic in card_list:

        # 判断当循环到的name键值是否等于等于find_name
        if card_dic["name"] == find_name:
            # 如果等于，将字典的信息以字符串的方式输出
            for card_str in card_dic:
                print(f"{card_str}是：{card_dic[card_str]}", end=" \t")
            print()
            # 如果找到，应该直接退出循环，不再遍历后续的元素（节省资源）
            break
    # 如果查询不到，输出 查无此人！
    else:
        # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
        # 还希望有一个统一的提示，此时就使用for + else 组合
        print("查无此人！")
        print()
