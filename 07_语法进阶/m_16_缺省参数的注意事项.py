"""
缺省参数的注意事项
1) 缺省参数的定义位置
必须保证 带有默认值的缺省参数 在参数列表末尾
2) 调用带有多个缺省参数的函数
在 调用函数时，如果有 多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系！
"""


# 1) 缺省参数的定义位置
# 如： def print_info(name, gender=True, title)
# 此时会报错，提示更换title的位置
# 两个缺省参数同时使用
def print_info(name, title="无", gender=True):
    """

    :param title: 职位
    :param name: 班上同学姓名
    :param gender:True为男生，False为女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    if title == "无":
        print("%s 是 %s" % (name, gender_text))

    else:
        print("%s 是 %s  [%s]" % (name, gender_text, title))


print_info("小青", "班长", False)

# 2) 调用带有多个缺省参数的函数
# 有多个缺省参数，调用时使用缺省参数默认值，其他缺省参数在使用时需要指定参数名
print_info("小米", gender=False)

