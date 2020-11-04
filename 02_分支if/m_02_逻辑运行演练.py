# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
# 要求人的年龄在 0-120 之间
age = int(input("请输入年龄："))
if age>=0 and age <= 120:
    print("年龄输入正确")
else:
    print("年龄输入错误")
print("要求年龄在0-120之间")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
# 要求只要有一门成绩 > 60 分就算合格
python_score = float(input("科学成绩是："))
c_score = float(input("数据成绩是："))

if python_score >= 60 or c_score >=60:
    print("成绩合格")
else:
    print("成绩不合格！")

# 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
# # 如果不是提示不允许入内
# is_employee = bool(input("请刷卡："))
is_employee = True

if not is_employee:
    print("非本公司员工禁止入内")
else:
    print("请进！")


