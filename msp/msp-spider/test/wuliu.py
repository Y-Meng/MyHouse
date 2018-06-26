# -*- coding: utf-8 -*-
import copy

# 中转点中转站租赁费用 5个
zhong_zhuan_zhan = [1, 2, 3, 4, 5]
jian_she_fei = [7500, 8500, 9000, 9500, 8000]


# 回收点及回收量 27个
hui_shou_dian = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
hui_shou_liang = [153, 199, 172, 230, 153, 146, 167, 137, 151, 149, 229, 184, 153, 291, 138, 257, 214, 140, 160, 148, 121, 149, 139,
      180, 178, 138, 131]

# 中转站到处理中心距离
DISTANCE_C_Z = [1000, 1050, 2000, 2500, 1800]

# 回收点到中转站距离： M*N 矩阵
DISTANCE_Z_H = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    [6, 7, 8, 9, 10, 2, 3, 4, 5, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 3, 4, 5, 6, 7, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27],
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 11, 12, 13, 14, 4, 5, 6, 7, 8, 6, 7, 8, 9, 10, 26, 27],
    [21, 22, 23, 24, 25, 26, 27, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 5, 6, 7, 8, 5, 6]
]

# 回收点-回收点之间距离: N*N 矩阵
DISTANCE_H_H = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    [4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8],
    [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7],
    [22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
    [23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],
    [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3],
    [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2],
    [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# 回收点分组 [[], [], ...]
hui_shou_zu = []
hui_shou_ju_li = []
# 回收组中转站
global hui_shou_zu_zzz
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


# -----------------------算法第一阶段计算模型初始解-----------------------------------------------------
def part1():
    group_collection_point()  # 回收站分组
    match_transfer_point()  # 分配中转站与分组
    optimize_path()  # 优化内部路径


# 1.将所有回收点分组
def group_collection_point():
    k = 0
    hui_shou_zu.append([])
    while len(hui_shou_dian) > 0:
        selected = get_next_index(k)
        while not more_than_v(k):
            if len(hui_shou_dian) > 0:
                hui_shou_zu[k].append(hui_shou_dian[selected])
                hui_shou_dian.pop(selected)
                selected = get_next_index(k)  # 获取下一个回收点（最小边际成本原则）
            else:
                break
        if len(hui_shou_dian)>0:
            k += 1
            hui_shou_zu.append([])
            hui_shou_zu[k].append(hui_shou_dian[selected])
            hui_shou_dian.pop(selected)
    print "回收点分组"
    print hui_shou_zu


# 2.分配中转站与分组（最小成本原则）
def match_transfer_point():
    k = len(hui_shou_zu)
    for i in range(0, k):
        zzz_index = min_collect_cost(i)   # 获取最小回收成本的中转站
        hui_shou_zu_zzz[zzz_index].append(i)
    print "中转站分组"
    print hui_shou_zu_zzz


# todo 3.优化回收组内部路径（图的最小环），实际图为非全联通图；这里简化仅计算各回收点到中转站距离之和
def optimize_path():
    for k in range(len(hui_shou_zu_zzz)):
        distance = 0
        for i in range(0, len(hui_shou_zu_zzz[k])):
            for n in range(0, len(hui_shou_zu[hui_shou_zu_zzz[k][i]])):
                distance += DISTANCE_Z_H[k][hui_shou_zu[hui_shou_zu_zzz[k][i]][n]-1]
        hui_shou_ju_li.append(distance)
    print "回收组优化路径"
    print hui_shou_ju_li


# 计算最小回收成本中转站
def min_collect_cost(k):
    min_index = 0
    min_cost = 0
    for i in range(0, len(zhong_zhuan_zhan)):
        cost = 0
        for j in range(0, len(hui_shou_zu[k])):
            p = hui_shou_zu[k][j]
            cost += shou_ji_che_c * hui_shou_liang[p-1] * (DISTANCE_Z_H[i][p-1] - 1)
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
        count += (hui_shou_liang[hui_shou_zu[k][i]-1])
        i += 1
    return count > shou_ji_che_v


# 获取下一个回收点（满足边际成本最小）
def get_next_index(k):
    start = 8  # 随机开始索引
    if len(hui_shou_dian) == 27:
        return start
    else:
        return min_marginal_cost(k)


# 最小边际成本计算(到组内所有点最近的点，还需要所有回收点之间距离）
def min_marginal_cost(k):
    min_index = 0
    min_value = 0
    for i in range(0, len(hui_shou_dian)):
        value = 0
        for j in range(0, len(hui_shou_zu[k])):
            value += DISTANCE_H_H[hui_shou_dian[i]-1][hui_shou_zu[k][j]-1]
        if min_value == 0 or min_value > value:
            min_value = value
            min_index = i
    return min_index


# ---------------------------------算法第二阶段----------------------------------------------------------------------
def part2():
    # 各中转站总体费用
    min_cost = total_cost()

    # 启发式优化（轮流其中一个中转站）
    temp_zzz = copy.deepcopy(hui_shou_zu_zzz)
    for i in range(0, len(temp_zzz)):
        # 关闭一个中转站，重新分配其中的分组
        for n in range(0, len(temp_zzz)):
            hui_shou_zu_zzz[n] = copy.copy(temp_zzz[n])

        while len(hui_shou_zu_zzz[i]) > 0:
            min_index = min_collect_cost_2(hui_shou_zu_zzz[i][0], i)
            hui_shou_zu_zzz[min_index].append(hui_shou_zu_zzz[i][0])
            hui_shou_zu_zzz[i].pop(0)

        # 重新优化路径
        optimize_path()
        # 新的总体费用
        cost = total_cost()
        print "close：%d" % i
        print "cost：%d" % cost
        if min_cost > cost:
            min_cost = cost

    print "最终分组和费用："
    print hui_shou_zu_zzz
    print min_cost


# 计算最小收集费用中转站（关闭其中一个中转站close_index）
def min_collect_cost_2(k, close_index):
    min_index = 0
    min_cost = 0
    for i in range(0, len(zhong_zhuan_zhan)):
        cost = 0
        if i != close_index:
            for j in range(0, len(hui_shou_zu[k])):
                p = hui_shou_zu[k][j]
                cost += shou_ji_che_c * hui_shou_liang[p-1] * (DISTANCE_Z_H[i][p-1] - 1)
        else:
            cost = 999999999

        if min_cost == 0 or cost < min_cost:
            min_cost = cost
            min_index = i

    return min_index


# 总费用
def total_cost():
    cost = []
    total_cost_value = 0
    for i in range(0, len(hui_shou_zu_zzz)):
        if len(hui_shou_zu_zzz[i]) > 0:
            cost.append(shou_ji_total_cost(i) + yun_shu_che_c * DISTANCE_C_Z[i] * yun_shu_che_v)
            total_cost_value += cost[i]
        else:
            cost.append(0)

    print "各中转站费用"
    print cost
    print "总费用"
    print total_cost_value
    return total_cost_value


# 中转站总体费用
def shou_ji_total_cost(k):
    # 建设费 + 分组收集费 + 库存费
    cost = (jian_she_fei[k] + shou_ji_cost(k) + ku_cun_cost(k))
    return cost


# 中转站总体收集费用
def shou_ji_cost(k):
    cost = 0
    for i in range(0, len(hui_shou_zu_zzz[k])):
        for j in range(0, len(hui_shou_zu[i])):
            cost += (shou_ji_che_c * hui_shou_liang[hui_shou_zu[i][j]-1] * hui_shou_ju_li[j])
    return cost


# 中转站库存费用
def ku_cun_cost(k):
    cost = ku_cun_c * 300
    return cost

# 主函数
if __name__ == '__main__':
    part1()
    part2()
