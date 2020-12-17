import cards_tools

# 设置一个无限循环体，由用户决定什么时候退出系统！
while True:
    # TODO(MU) 展示菜单功能  (用TODO标记还没有做但是需要去做的工作)
    cards_tools.show_menu()

    action = input("请选择操作功能：")

    # 1，2,3针对名的操作
    if action in ["1", "2", "3"]:

        # 新增名片
        if action == "1":
            # 当输入为"1"时，调用新建名片函数
            cards_tools.new_menu()

        # 显示全部名片
        elif action == "2":
            # 当输入为"2"时，调用显示全部函数
            cards_tools.show_all()

        # 查询名片
        else:
            # 当输入为"3"时，调用查询名片函数
            cards_tools.search_card()
            # cards_tools.deal_card()

    # 当输入为"0"时，退出名片管理系统
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    else:
        print("输入错误，请重新输入！")
