'''

使用大M法单纯型法
函数形式为min

Simplex method to solve linear programming models, implemented using big M method


reference : https://github.com/david-toro/SimplexMethod/blob/master/simplex/simplex.py
            https://wenku.baidu.com/view/9cb1776d27d3240c8447efc8.html
'''

import  numpy as np

def simplex(type, A, B, C, D, M):
    """Calculates an optimal point for the linear programming model given by A*x <= B , Optimize z= C' * x
    Arguments:
    type -- type of optimization, it can be 'max' or 'min'
    A    -- A matrix of the model (numpy array)                           左侧项模型
    B    -- B matrix of the model, column vector (numpy array)           右侧项模型
    C    -- C matrix of the model, column vector (numpy array)           目标函数
    D    -- column vector with the types of restrictions of the model (numpy array),  各约束的符号
            1 is <=, 0 is =, -1 is >=
            for <= restrictions do nothing
            for = restrictions add an artificial variables and a big M in the objective
            function (min --> +M , max --> -M)
            for >= restrictions multiply by -1
    M    -- big M value

    大M法 对松弛后的等式问题，使用-M进行限制
    """

    (m,n)=A.shape   # m,n分别表示模型A的约束个数 和 变量个数

    #记录新模型的变量个数
    variableCount = n

    # 记录基变量的下标,从0开始
    basic_vars =[]

    '''
    构造新的模型表示
    '''
    for i in range (m):
        if D[i]== 1:
            # 约束为<=,添加松弛变量，目标函数上加一个0
            C= np.vstack(C, [[0]])  #垂直顺序堆叠（按照行顺序）

            #选取基变量
            variableCount +=1
            basic_vars = basic_vars+[variableCount-1]





        elif D[i] == 0:
            #约束为=，添加M
            C=np.vstack(C,[[M]])

            variableCount += 1
            basic_vars = basic_vars + [variableCount - 1]


        else:
            #约束为>=,添加松弛变量和M
            C = np.vstack(C, [[0],[M]])

            variableCount += 2
            basic_vars = basic_vars + [variableCount - 1]
