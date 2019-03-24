#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from operator import attrgetter

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


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
        items.append(Item(i - 1, int(parts[0]), int(parts[1]), 1.0 * int(parts[0])/int(parts[1])))

    value , taken = dynamicProgramming(capacity, items)


    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def greedy(capacity, items):
    n = len(items)
    value =0
    taken = [0]*n
    filledWeight =0
    for item in sorted(items, key=attrgetter('density')):
        if(filledWeight + item.weight <=capacity):
            value +=item.value
            taken[item.index]=1
            filledWeight += item.weight
        else:
            break
    return  value, taken

def dynamicProgramming(capacity, items):
    n= len(items)
    taken =[0]*n
    values = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

    for j in range (1, n+1):
        for K in range(1, capacity+1):
            value = items[j-1].value
            weight = items[j-1].weight

            if weight >K:
                values[j][K] = values[j-1][K]
            else:
                vTake= values[j-1][K-weight]+value
                vNotTake= values[j-1][K]
                values[j][K] = max(vTake, vNotTake)

    # 确定最优解
    totalWeight = capacity
    for j in reversed(range(n)):
        if values[j][totalWeight]== values[j-1][totalWeight]:
            continue
        else:
            taken[j] =1
            totalWeight -=items[j].weight

    return values[-1][-1], taken





if __name__ == '__main__':
    file_location = "C:/Users/Administrator/Desktop/Ramanuyan/DiscreteOptimization/Knapsack/ks_4_0"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()
    solve_it(input_data)
    print(solve_it(input_data))
else:
    print('This test requires an input file.  Please select one from the data directory. (i.e. python solverCopy.py ./data/ks_4_0)')



'''

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
'''