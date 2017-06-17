'''
# 遍历索引遍历元素
ls = [1, 2, 3, 4, 5]
for index, item in enumerate(ls):
    print(index, item)

# 计算文件行数

##方法1
count = len(open('file1.txt', 'r').readlines())
print(count)

##方法2
for count, line in enumerate(open('file1.txt', 'r'), 1):
    pass
print(count)

##方法3
count = len(list(enumerate(open('file1.txt', 'r'))))
print(count)

'''


# filter,map,reduce,lamda


# --------------filter
def f(x):
    return x % 2 != 0 and x % 3 != 0


res = list(filter(f, range(2, 25)))
print(res)
res = list(filter(None, range(1, 5)))
print(res)


# --------------map
def cube(x):
    return x * x * x


res = list(map(cube, range(1, 5)))
print(res)


def add(x, y):
    return x + y


res = list(map(add, range(5), range(5)))
print(res)


def func(x, y):
    return x, y


num = [0, 1, 2, 3, 4, 5, 6]
weekday = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
res = list(map(func, num, weekday))
print(res)

# --------------reduce
from functools import reduce

res = reduce(lambda x, y: x + y, range(1, 101))
print(res)
