# -*- coding: utf-8 -*-

# 中转点中转站租赁费用 5个
zhong_zhuan_zhan = [1, 2, 3, 4, 5]
zu_lin_fei = [7500, 8500, 9000, 9500, 8000]


# 回收点及回收量 27个
hui_shou_dian = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
hui_shou_liang = [153, 199, 172, 230, 153, 146, 167, 137, 151, 149, 229, 184, 153, 291, 138, 257, 214, 140, 160, 148, 121, 149, 139,
      180, 178, 138, 131]

# 回收点到中转站距离
DISTANCE_Z_H = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    [6, 7, 8, 9, 10, 2, 3, 4, 5, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 3, 4, 5, 6, 7, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27],
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 11, 12, 13, 14, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10, 26, 27],
    [21, 22, 23, 24, 25, 26, 27, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 5, 6, 7, 8, 5, 6]
]

# 回收点分组 [[], [], ...]
hui_shou_zu = []
# 回收组中转站
hui_shou_zu_zzz = [[], [], [], [], []]

# 收集车辆容量和成本
shou_ji_che_v = 600
shou_ji_che_c = 0.01

# 运输车辆容量和成本
yun_shu_che_v = 2000
yun_shu_che_c = 0.02

# 库存成本
ku_cun_c = 0.05

# 处理成本
chu_li_c = 0.02

# 处理周期T天
T = 300


# -----算法第一阶段计算模型初始解-----
def part1():
    group_collection_point()  # 回收站分组
    match_transfer_point()  # 分配中转站与分组
    optimize_path()  # 优化内部路径


# 1.将所有回收点分组
def group_collection_point():
    k = 0
    hui_shou_zu.append([])
    while len(hui_shou_dian) > 0:
        selected = get_next_index()
        while not more_than_v(k):
            hui_shou_zu[k].append(hui_shou_dian[selected])
            hui_shou_dian.pop(selected)
            selected = get_next_index()  # 获取下一个回收点（最小边际成本原则）
        k += 1
        hui_shou_zu.append([])
        hui_shou_zu[k].append(hui_shou_dian[selected])
        hui_shou_dian.pop(selected)


# 2.分配中转站与分组（最小成本原则）
def match_transfer_point():
    k = len(hui_shou_zu)
    for i in range(0, k-1):
        zzz_index = min_collect_cost(i)   # 获取最小回收成本的中转站
        hui_shou_zu_zzz[zzz_index].append(i)


# todo 3.优化回收组内部路径（图的最小生成树？）
def optimize_path():
    return 0


# 计算最小回收成本中转站
def min_collect_cost(k):
    min_index = 0
    min_cost = 0
    for i in range(0, len(zhong_zhuan_zhan)):
        cost = 0
        for j in range(0, len(hui_shou_zu[k])):
            p = hui_shou_zu[k][j]
            cost += shou_ji_che_c * hui_shou_liang[p-1] * DISTANCE_Z_H[i][p-1]
        if min_cost == 0 or cost < min_cost:
            min_cost = cost
            min_index = i

    return min_index


# 判断回收量之和是否超过收集车辆总量
def more_than_v(k):
    count = 0
    i = 0
    size = len(hui_shou_zu[k])
    while i < size:
        count += hui_shou_zu[k][i]
        i += 1
    return count > shou_ji_che_v


# 获取下一个回收点（满足边际成本最小）
def get_next_index():
    start = 8  # 随机开始索引
    if len(hui_shou_dian) == 27:
        return start
    else:
        return min_marginal_cost()


# todo 最小边际成本计算
def min_marginal_cost():
    return 0


# 主函数
if __name__ == '__main__':
    part1()
