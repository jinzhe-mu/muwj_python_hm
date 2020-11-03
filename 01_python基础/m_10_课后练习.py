"""
需求:
在控制台依次提示用户输入：姓名、公司、职位、电话、邮箱
按照以下格式输出：
**************************************************
公司名称
​
姓名 (职位)
​
电话：电话
邮箱：邮箱
**************************************************
"""
name = input("请输入姓名：")
company = input("请输入公司的名称：")
title = input("请输入职位：")
phone = input("请输入电话：")
email = input("请输入邮箱：")
print("*" * 50)
print("%s" % company)
print()
print(" %s（%s）" % (name, title))
print()
print("电话%s" % phone)
print("邮箱：%s" % email)
print("*" * 50)
