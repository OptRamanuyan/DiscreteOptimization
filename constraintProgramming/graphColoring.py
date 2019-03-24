#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))


    solution = [0]*node_count
    j=1
    while j > 0:      # node 0颜色为0 从node 1开始
        # solution[j]= solution[j]+1
        while (solution[j]<node_count and not conflict(edges, solution,j)):
            solution[j] = solution[j] + 1
        if (j < node_count-1): #不是最后一个点
            j=j+1
            solution[j]=0
        else:
            break
    color = max(solution)
    # prepare the solution in the specified output format
    output_data = str(color+1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


def conflict(edges, solution,j):   #判断solution[j] 和j之前的点  是否冲突
    # 看edge中j与哪个有连接，颜色是否一致
    for i in range (len(edges)):
        if j == edges[i][1]:  # j是连线中的第二个点，判断两点的颜色是否一致
            k = edges[i][0]
            if (solution[j]== solution[k]):
                return  False
    return True
#
if __name__ == '__main__':
    import  sys

    file_location = "C:/Users/Administrator/Desktop/Ramanuyan/DiscreteOptimization/constraint programming/coloring/data/gc_4_1"
    with open(file_location, 'r') as input_data_file:
        input_data = input_data_file.read()

    print(solve_it(input_data))



#
# if __name__ == '__main__':
#     import sys
#     if len(sys.argv) > 1:
#         file_location = sys.argv[1].strip()
#         with open(file_location, 'r') as input_data_file:
#             input_data = input_data_file.read()
#         print(solve_it(input_data))
#     else:
#         print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
#
#
#