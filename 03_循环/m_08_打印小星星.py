"""
需求:
在控制台连续输出五行 *，每一行星号的数量依次递增
*
**
***
****
*****
使用字符串 * 打印
"""

# j = 0
# k = "*"

# while j < 10:
#     i = "*"
#     i *= j
#     k += i
#     print(k)
#     j += 1


row = 1
while row <= 10:
    print("*" * row)
    row += 1
