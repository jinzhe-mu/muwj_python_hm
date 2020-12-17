# 记录所有的名片字典
card_list = []


# 显示菜单
def show_menu():
    """    显示菜单    """
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
    """      新建名片      """
    print("*" * 50)
    print("功能：新建用户名片")

    # 1. 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入手机：")
    qq_str = input("请输入QQ号：")
    email_str = input("请输入邮箱：")
    # 2. 将用户信息保存到一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str
                 }

    # 3. 将用户字典添加到名片列表
    card_list.append(card_dict)
    print(card_dict)

    # 4. 提示添加成功信息
    print(f"已成功添加 “{card_dict['name']}” 的名片")


# 显示全部名片
def show_all():
    """    显示全部名片    """
    print("*" * 50)
    print("功能：搜索名片")

    # 1. 判断是否有名片记录
    if len(card_list) == 0:
        print("提示：没有任何名片记录")

        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return后面没有没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何结果
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
    """搜索名片
    搜索已有名片系统中指定的信息
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
    从列表中查找名片
    :return:
    """
    print()
    find_name = input("请输入查找人姓名：")
    print("-" * 50)
    # 循环所有字典进行查找
    for card_dic in card_list:

        # 判断当循环到的name键值是否等于等于find_name
        if card_dic["name"] == find_name:
            # 如果等于，将字典的信息以字符串的方式输出

            print("姓名\t\t\t\t手机\t\t\t\tQQ\t\t\t\t邮箱")
            print("-" * 50)
            print("%s\t\t\t\t%s\t\t\t%s\t\t%s" % (card_dic["name"],
                                                  card_dic["phone"],
                                                  card_dic["qq"],
                                                  card_dic["email"]))

            print()
            # 如果找到，应该直接退出循环，不再遍历后续的元素（节省资源）

            # TODO 针对搜索到的名片进行修改删除操作（当功能完成后，把TODO标记删除）
            # 调用处理名片函数对名片进行处理
            deal_card(card_dic)  # 将实参card_dic传给形参find_dict

            break

            # 修改、删除名片

    # 如果查询不到，输出 查无此人！
    else:
        # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
        # 还希望有一个统一的提示，此时就使用for + else 组合
        print("查无此人！")
        print()


# 处理名片
def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict:用户查询到的名片信息
    :return:
    """
    print("*" * 50)

    action_str = input("请选择要执行的操作 "
                       " 修改-[1] \ 删除-[2] \ 返回上级菜单-[0]  :")

    if action_str == "1":
        print("*" * 50)
        print("修改一下信息：如果不修改的回车跳过")
        # find_dict["name"] = input("修改姓名：")
        # find_dict["phone"] = input("修改手机号：")
        # find_dict["qq"] = input("修改QQ号：")
        # find_dict["email"] = input("修改邮箱：")

        # 调用input_card_info（）函数进行输入细节处理
        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改手机号：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "修改QQ号：")
        find_dict["email"] = input_card_info(find_dict["email"], "修改邮箱：")
        """
        如果用户在使用时，某些名片内容并不想修改，应该如何做呢？
        —— 既然系统提供的 input 函数不能满足需求，
        那么就新定义一个函数 input_card_info 对系统的 input 函数进行扩展
        """

        print("姓名\t\t\t\t手机\t\t\t\tQQ\t\t\t\t邮箱")

        print("%s\t\t\t\t%s\t\t\t%s\t\t%s" % (find_dict["name"],
                                              find_dict["phone"],
                                              find_dict["qq"],
                                              find_dict["email"]))
        print("信息修改成功！")

    elif action_str == "2":
        print("*" * 50)
        card_list.remove(find_dict)
        print("%s相关信息删除成功！" % find_dict["name"])
        print()


# 修改名片内容细化，使用此函数替换修改信息时的input函数
def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回输入内容，否则返回字典原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str
    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:

        return dict_value
