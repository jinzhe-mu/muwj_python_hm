"""
需求:
从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
比较胜负
序号	规则
1	石头 胜 剪刀
2	剪刀 胜 布
3	布 胜 石头
"""
import random

while True:
    while True:
        player = int(input("请出拳 石头（1）/剪刀（2）/布（3）："))
        computer = random.randint(1, 3)  # 取随机数1到3
        if ((player == 1 and computer == 2) or
                (player == 2 and computer == 3) or
                (player == 3 and computer == 1)):
            print("电脑出的是{}".format(computer))
            print("玩家赢了！电脑输的一败涂地！")
            break

        elif player == computer:
            print("小样，竟然打成平手了，再来一局！")
            break
        else:
            print("电脑出的是{}".format(computer))
            print("玩家弱爆了，电脑赢了！！")
            break

    print("还要再来一局吗，哈哈哈哈哈!!!!")
    choice = input("请选择：Y/N:")
    if choice == "Y":
        print("比赛继续")
        continue
    else:
        print("比赛结束")
        break

