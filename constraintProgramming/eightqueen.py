
'''
backtrack  回溯法
'''

def check (queen, i,col):
    if(i==0):
        return True
    else:
        for k in range (i) :
            if(col==queen[k] or abs(col- queen [k])==i-k):
                return False   # 冲突

    return  True


def eightQueen ():
    n=8
    queen = [0 for i in range(n)]
    i=0
    while (i<n):        # 放置第i行的皇后
        col = queen[i]  #遍历第i行皇后的位置
        while (col<n):
            if(check(queen,i,col)): # 不冲突，此列可以放皇后
                queen[i]=col   #放置
                i=i+1
                break    # 不再继续运行，结束当前循环 回到while(i<n) 进行下一次循环
            col=col+1   #冲突，选择下一col

        # 遍历到第8列，仍然无法放置，需要回溯
        if(col==n):
            queen[i]=0
            i=i-1
            if(queen[i]==n-1):  #若上一行放置在第8列，说明无法移动此行的皇后，需要再往上回溯一行
                if(i==0):  # 无解
                    # print("无解")
                    break       #直接跳出，程序结束
                else:
                    queen[i]=0
                    i=i-1
                    queen[i] += 1
            else:    #当前行的皇后往后走一列
                queen[i]+=1


        if(i==n):
            printm(n,queen)
            i -= 1  # 继续寻找下一个解
            if (queen[i] == n - 1):  # 上一行皇后放在最后一列则不能直接往后移动一列，需要再次回溯
                queen[i] = 0
                i -= 1
                queen[i] += 1
            else:
                queen[i] += 1


def printm(n,queen):
    for k in range(n):
        j = 0
        while (j < queen[k]):
            print('O', end=' ')
            j += 1
        print('X', end=' ')
        j += 1
        while (j < n):
            print('O', end=' ')
            j += 1
        print( )
    print('-------------------')

if __name__ == '__main__':
    eightQueen()





