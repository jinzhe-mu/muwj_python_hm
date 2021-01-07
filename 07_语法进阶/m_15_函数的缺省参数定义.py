# 将gender默认为True，输入时忽略既为默认为True
def print_info(name, gender=True):
    """

    :param name: 班上同学姓名
    :param gender:True为男生，False为女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# print_info("小明", True)
# 如果班上男生居多，想要将为男生时定义成缺省参数
# 提示：在指定缺省参数默认值时，应该使用最常见的值作为默认值！
print_info("小强")
print_info("小青", False)