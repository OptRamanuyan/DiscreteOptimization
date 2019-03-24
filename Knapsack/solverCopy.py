#!/usr/bin/python3
# -*- coding: utf-8 -*-


from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full


    # value, opt, take = dp(capacity, items)
    value, take = DP(capacity, item_count, items)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, take))
    return output_data


def DP(capacity, item_count, items):
    s = [([0] * (capacity + 1)) for i in range(item_count + 1)]
    take = [0] * item_count

    for i in range(1, item_count + 1):
        for k in range(1, capacity + 1):
            if (items[i - 1].weight > k):
                s[i][k] = s[i - 1][k]
            else:
                vkeep = s[i - 1][k]
                vTake = s[i - 1][k - items[i - 1].weight] + items[i - 1].value
                s[i][k] = max(vkeep, vTake)
    k = capacity
    for i in range(item_count, 0, -1):
        if (k == 0):
            break
        if (s[i][k] == s[i - 1][k]):
            take[i - 1] = 0
            k = k - 1
        else:
            take[i - 1] = 1
            k = k - items[i - 1].weight

    value = s[-1][-1]
    return value, take

#
# if __name__ == '__main__':
#     import sys
#
#     if len(sys.argv) > 1:
#         file_location = sys.argv[1].strip()
#         with open(file_location, 'r') as input_data_file:
#             input_data = input_data_file.read()
#         print(solve_it(input_data))
#     else:
#         print(
#             'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')


def dp(cap, items):
    n = len(items)
    taken = [0] * n
    values = [[0 for j in range(cap + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        if i > 0:
            value = items[i - 1].value
            weight = items[i - 1].weight
        for j in range(cap + 1):
            if i == 0 or j == 0:
                continue
            elif weight > j:
                values[i][j] = values[i - 1][j]
            else:
                vTake = values[i - 1][j - weight] + value
                vKeep = values[i - 1][j]
                values[i][j] = max(vTake, vKeep)

    totalWeight = cap
    for i in reversed(range(n)):
        if values[i][totalWeight] == values[i + 1][totalWeight]:
            continue
        else:
            taken[i] = 1
            totalWeight -= items[i].weight

    return values[-1][-1], 1, taken

if __name__ == '__main__':
    file_location = "C:/Users/Administrator/Desktop/Ramanuyan/DiscreteOptimization/Knapsack/homework/data/ks_40_0"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    solve_it(input_data)
    print(solve_it(input_data))
else:
    print('This test requires an input file.  Please select one from the data directory. (i.e. python solverCopy.py ./data/ks_4_0)')