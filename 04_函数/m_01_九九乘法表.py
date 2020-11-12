def multiple_table(row, col):
    while row <= 9:
        # 阶梯式乘法口诀，判断i和j的大小，不重复输出
        while row >= col:
            # end("")表示输出后不换行，下一次输出在同一行
            # 增加转义字符，\t：在控制台输出一个 制表符，协助在输出文本时 垂直方向 保持对齐
            print("%d * %d =" % (col, row), row * col, end="\t")
            col += 1

        row += 1  # 将乘数的值递增
        col = 1  # 将被乘数的值重置

        # 直接输出print("")表示换行
        print("")


# multiple_table(1, 1)
