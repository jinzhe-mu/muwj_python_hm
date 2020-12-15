card_list = []


def show_all():
    """
    显示全部名片
    """
    print("*" * 50)
    print("功能：搜索名片")
    if len(card_list) == 0:
        print("提示：没有任何名片记录")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t\t")
    print()
    print("-" * 50)

    for card_dic in card_list:

        for card_str in card_dic:
            print(f"{card_dic[card_str]}", end="\t\t\t")

        print()

    # for card_dict in card_list:
    #
    #     print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
    #                                     card_dict["phone"],
    #                                     card_dict["qq"],
    #                                     card_dict["email"]))


show_all()
