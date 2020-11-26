"""
Python 包含了以下内置函数：
函数	                描述	                            备注
len(item)	        计算容器中元素个数
del(item)	        删除变量	del                     有两种方式
max(item)	        返回容器中元素最大值	            如果是字典，只针对 key 比较
min(item)	        返回容器中元素最小值	            如果是字典，只针对 key 比较
cmp(item1, item2)	比较两个值，-1 小于/0               相等/1 大于	Python 3.x 取消了 cmp 函数
注意:
字符串 比较符合以下规则： "0" < "A" < "a"
"""
a = [0, 1, 2, 3, 4, 5, 6]
b = {"0", "1", "2", "3", "4", "h", "e", "A", "a"}
d = {"name": "小明",
     "age": 18,
     "gender": True,
     "height": 180,
     "weight": 140
     }
c = "0aA"

# 计算长度,列表、字典、字符共用
print(len(a), len(b), len(d))  # 7 9 5

# del 的两种用法
del (a[0])  # [1, 2, 3, 4, 5, 6]
del a[1]  # [1, 3, 4, 5, 6]
del d["age"]  # {'name': '小明', 'gender': True, 'height': 180, 'weight': 140}

print(a, b, c, d)

# del a  # 等价于del(a)
# print(a)  # 列表a被直接删除

# 比较大小（只有同一种数据类型的才能做比较）,如果是字典，只针对 key 比较
print(max(b))  # h
print(max(c))  # a
print(max(a))  # 6
print(max(d))  # weight

print(min(b))  # 0
print(min(c))  # 0
print(min(a))  # 1
print(min(d))  # age

