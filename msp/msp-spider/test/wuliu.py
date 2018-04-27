# -*- coding: utf-8 -*-

# 中转点中转站租赁费用 5个
R = [1, 2, 3, 4, 5]
Dc = [7500, 8500, 9000, 9500, 8000]


# 回收点及回收量 27个
J = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
Cv = [153, 199, 172, 230, 153, 146, 167, 137, 151, 149, 229, 184, 153, 291, 138, 257, 214, 140, 160, 148, 121, 149, 139,
      180, 178, 138, 131]
# 回收点分组
GC = [[], [], [], [], []]

# 运输成本
C0 = 0.01
C1 = 0.02

# 收集车辆容量
Wc = 600

# 运输车辆容量
Ct = 2000

# 库存成本
Dc = 0.05

# 处理成本
Hc = 0.02

# 处理周期T天
T = 300


# 算法第一阶段计算模型初始解
def part1():
    group_collection_point()


# 将所有回收点分组
def group_collection_point():
    start = 8
    GC[0].append(J[start])
    J.pop(start)

    k = 0
    while len(J) > 0:
        selected = get_next()
        while not more_than_v(k):
            GC[k].append(J[selected])
            J.pop(selected)
            selected = get_next()
        k += 1
        GC[k].append(J[selected])
        J.pop(selected)


# 判断回收量之和是否超过收集车辆总量
def more_than_v(k):
    count = 0
    for i in GC[k]:
        count += GC[k][i]
    return count > Ct


# 获取下一个回收点（满足边际成本最小）
def get_next():
    return 0
