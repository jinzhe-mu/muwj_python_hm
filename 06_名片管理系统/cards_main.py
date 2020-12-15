import cards_tools


# 设置一个无限循环体，让用户决定退出时间
while True:
    # 一开始就先展示菜单
    cards_tools.show_menu()

    action = input("请选择操作功能：")

    if action in ["1", "2", "3"]:

        if action == "1":
            # 当输入为“1”时，调用新建名片函数
            cards_tools.new_menu()

        elif action == "2":
            # 当输入为“2”时，调用显示全部函数
            cards_tools.show_all()

        else:
            # 当输入为“3”时，调用查询名片函数
            cards_tools.search_card()

    # 当输入为“0”时，退出名片管理系统
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    else:
        print("输入错误，请重新输入！")







