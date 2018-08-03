# -*- coding: utf-8 -*-
import copy

# 中转点中转站租赁费用 5个
zhong_zhuan_zhan = [1, 2, 3, 4]
jian_she_fei = [7500, 8500, 9000, 9500]


# 回收点及回收量 27个
hui_shou_dian = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
hui_shou_liang = [153, 199, 172, 230, 153, 146, 167, 137, 151, 149, 229, 184, 153, 291, 138, 257, 214, 140, 160, 148, 121]

# 中转站到处理中心距离
DISTANCE_C_Z = [10, 11, 20, 25]

# 回收点到中转站距离： M*N 矩阵
DISTANCE_Z_H = [
    [4.9, 3.7, 5.8, 3.5, 1.3, 3.3, 1.6, 2.2, 1.5, 1.5, 0.48, 1.5, 1.7, 2.4, 2.3, 4.7, 4.5, 3.4, 3.5, 4.7, 5.3],
    [4.3, 4.2, 5.3, 2.8, 3.0, 5.0, 2.2, 3.8, 2.2, 2.2, 1.9, 0.56, 2.5, 1.3, 0.3, 3.0, 2.4, 2.3, 2.3, 2.8, 3.0],
    [5.6, 5.9, 6.9, 3.7, 4.1, 6.1, 3.2, 4.7, 3.1, 3.1, 2.8, 2.0, 3.4, 2.2, 1.3, 1.8, 1.4, 2.9, 2.1, 1.9, 1.8],
    [6.9, 6.7, 7.8, 6.0, 5.2, 9.4, 3.7, 5.1, 3.5, 4.0, 3.8, 3.1, 3.0, 3.1, 3.0, 4.0, 1.7, 1.8, 0.81, 0.7, 1.3]
]

# 回收点-回收点之间距离: N*N 矩阵, 999为最大占位值，无实际意义
DISTANCE_H_H = [
    [999, 1.1, 3.1, 2.3, 3.5, 6.4, 5.5, 6.4, 6.1, 5.1, 5.6, 4.3, 6.3, 5.2, 4.6, 5.7, 6.8, 6.2, 6.2, 7.4, 6.5],
    [1.1, 999, 3.5, 2.2, 2.3, 5.2, 4.3, 5.2, 4.9, 3.9, 4.5, 4.2, 5.1, 5.4, 4.4, 6.0, 6.5, 6.0, 6.1, 7.0, 6.8],
    [3.1, 3.5, 999, 3.3, 4.5, 7.3, 6.4, 7.4, 7.1, 5.8, 6.5, 5.3, 7.3, 6.1, 5.5, 7.1, 8.7, 7.1, 7.1, 8.1, 7.8],
    [2.3, 2.2, 3.3, 999, 2.3, 5.0, 4.1, 5.0, 4.7, 3.7, 4.0, 2.8, 4.9, 3.6, 3.0, 3.8, 4.9, 4.6, 4.6, 5.6, 4.6],
    [3.5, 2.3, 4.5, 2.3, 999, 2.8, 1.9, 2.8, 2.5, 1.5, 2.1, 2.1, 2.7, 2.7, 3.2, 5.4, 4.9, 4.5, 4.5, 5.4, 5.5],
    [6.4, 5.2, 7.3, 5.0, 2.8, 999, 3.9, 4.9, 4.6, 3.5, 4.1, 4.1, 4.8, 4.7, 5.2, 7.4, 7.0, 6.6, 6.5, 7.5, 10.3],
    [5.5, 4.3, 6.4, 4.1, 1.9, 3.9, 999, 1.9, 0.65, 0.51, 1.2, 2.2, 0.86, 1.7, 2.5, 4.7, 4, 2.9, 3.7, 4.5, 4.6],
    [6.4, 5.2, 7.4, 5.0, 2.8, 4.9, 1.9, 999, 2.1, 2.1, 2.7, 3.0, 2.3, 3.2, 4.0, 6.2, 5.5, 3.8, 4.5, 5.7, 5.8],
    [6.1, 4.9, 7.1, 4.7, 2.5, 4.6, 0.65, 2.1, 999, 1.4, 1.1, 2.2, 0.71, 1.7, 2.5, 4.6, 3.9, 2.7, 3, 4.3, 4.4],
    [5.1, 3.9, 5.8, 3.7, 1.5, 3.5, 0.51, 2.1, 1.4, 999, 1.1, 2.0, 1.2, 1.7, 2.5, 4.6, 3.9, 3.3, 3.5, 4.4, 4.5],
    [5.6, 4.5, 6.5, 4.0, 2.1, 4.1, 1.2, 2.7, 1.1, 1.1, 999, 0.99, 1.4, 1.3, 2, 4.3, 3.6, 3.1, 3.1, 4.1, 4.2],
    [4.3, 4.2, 5.3, 2.8, 2.1, 4.1, 2.2, 3.0, 2.2, 2.0, 0.99, 999, 2.5, 1.4, 0.85, 3.6, 2.8, 2.4, 2.4, 3.3, 3.4],
    [6.3, 5.1, 7.3, 4.9, 2.7, 4.8, 0.86, 2.3, 0.71, 1.2, 1.4, 2.5, 999, 1.8, 2.7, 4.9, 4.2, 2.3, 2.5, 3.9, 4.0],
    [5.2, 5.4, 6.1, 3.6, 2.7, 4.7, 1.7, 3.2, 1.7, 1.7, 1.3, 1.4, 1.8, 999, 1.6, 3.7, 3.0, 2.4, 2.4, 3.5, 3.6],
    [4.6, 4.4, 5.5, 3.0, 3.2, 5.2, 2.5, 4.0, 2.5, 2.5, 2, 0.85, 2.7, 1.6, 999, 2.8, 2.1, 2.5, 2.5, 2.6, 2.7],
    [5.7, 6.0, 7.1, 3.8, 5.4, 7.4, 4.7, 6.2, 4.6, 4.6, 4.3, 3.6, 4.9, 3.7, 2.8, 999, 3.1, 4.7, 4.7, 3.6, 2.7],
    [6.8, 6.5, 8.7, 4.9, 4.9, 7.0, 4, 5.5, 3.9, 3.9, 3.6, 2.8, 4.2, 3.0, 2.1, 3.1, 999, 2.5, 2.4, 1.3, 1.4],
    [6.2, 6.0, 7.1, 4.6, 4.5, 6.6, 2.9, 3.8, 2.7, 3.3, 3.1, 2.4, 2.3, 2.4, 2.5, 4.7, 2.5, 999, 1.2, 2.5, 2.8],
    [6.2, 6.1, 7.1, 4.6, 4.5, 6.5, 3.7, 4.5, 3, 3.5, 3.1, 2.4, 2.5, 2.4, 2.5, 4.7, 2.4, 1.2, 999, 1.5, 2.2],
    [7.4, 7.0, 8.1, 5.6, 5.4, 7.5, 4.5, 5.7, 4.3, 4.4, 4.1, 3.3, 3.9, 3.5, 2.6, 3.6, 1.3, 2.5, 1.5, 999, 1.1],
    [6.5, 6.8, 7.8, 4.6, 5.5, 10.3, 4.6, 5.8, 4.4, 4.5, 4.2, 3.4, 4.0, 3.6, 2.7, 2.7, 1.4, 2.8, 2.2, 1.1, 999]
]

# 回收点分组 [[], [], ...]
hui_shou_zu = []
hui_shou_ju_li = []
# 回收组中转站
global hui_shou_zu_zzz
hui_shou_zu_zzz = [[], [], [], []]

# 收集车辆容量和成本
shou_ji_che_v = 800
shou_ji_che_c = 0.02

# 运输车辆容量和成本
yun_shu_che_v = 2500
yun_shu_che_c = 0.04

# 库存成本
ku_cun_c = 0.08

# 处理成本
chu_li_c = 0.06

# 处理周期T天
T = 30


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
        if len(hui_shou_dian) > 0:
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
        hui_shou_ju_li.append(int(distance))
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
            cost += shou_ji_che_c * hui_shou_liang[p-1] * (DISTANCE_Z_H[i][p-1])
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
    min_close_index = 0
    min_hui_shou_zzz = []

    print "*********启发式算法迭代***********"

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

        print "关闭分组：%d" % (i+1)

        # 重新优化路径
        optimize_path()
        # 新的总体费用
        cost = total_cost()
        print "关闭费用：%d" % cost
        print "*********************************"
        if min_cost > cost:
            min_cost = cost
            min_close_index = i+1
            min_hui_shou_zzz = copy.copy(hui_shou_zu_zzz)

    print "--------------最终分组和费用---------------------------------------"
    print "回收点分组："
    print hui_shou_zu
    print "回收组中转站分组："
    print min_hui_shou_zzz
    print "关闭分组：%d" % min_close_index
    print "最少费用：%d" % min_cost
    for i in range(0, len(min_hui_shou_zzz)):
        hui_shou = min_hui_shou_zzz[i]
        if len(hui_shou) > 0:
            temp_arr = []
            for n in range(0, len(hui_shou)):
                temp_arr = temp_arr + hui_shou_zu[hui_shou[n]]

            print '中转站 %d：' % (i+1)
            print temp_arr


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
            cost += (shou_ji_che_c * hui_shou_liang[hui_shou_zu[i][j]-1] * hui_shou_ju_li[i])
    return cost


# 中转站库存费用
def ku_cun_cost(k):
    cost = ku_cun_c * 300
    return cost


# 检查回收点距离数据
def check_data():
    print '----检查数据------------------------'
    for i in range(0, len(DISTANCE_H_H)):
        for j in range(0, i):
            DISTANCE_H_H[i][j] = DISTANCE_H_H[j][i]
        print DISTANCE_H_H[i]


# 主函数
if __name__ == '__main__':
    # check_data()

    print '----阶段一--------------------------'
    part1()
    print '----阶段二--------------------------'
    part2()
