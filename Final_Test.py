from multiprocessing.pool import ThreadPool
import time
pool = ThreadPool(processes=1)

"""
(0, 0) box 1
(0, 3) box 2
(0, 6) box 3
(3, 0) box 4
(3, 3) box 5
(3, 6) box 6
(6, 0) box 7
(6, 3) box 8
(6, 6) box 8
"""
A= [
     [1,4,5,2,8,3,7,9,6],
     [3,1,8,9,6,2,1,2,5],
     [2,6,9,1,5,7,4,8,3],
     [9,1,4,7,3,8,5,6,2],
     [6,8,3,5,1,2,9,4,7],
     [7,5,2,6,4,9,8,3,1],
     [4,3,6,8,7,1,2,5,9],
     [5,2,7,4,9,6,3,1,8],
     [8,9,1,3,2,5,6,7,4]
]

#return True if right & return the index if wrong
def Validation_of_rang_of_Board (Board):
    for i in range(9):
        for j in range(9):
            if Board[i][j] not in range(1,10):
                 return i,j
    return True
# return True if Right otherwise return the index
def Validation_of_num_of_column(Board,delay):
    time.sleep(delay)
    for i in Board:
        if(len(i)!=9):
            return Board.index(i)
    return True
#return True if right else return false
def Validation_of_num_of_rows(Board,delay):
    time.sleep(delay)
    if(len(Board)!=9):
        return False
    else:
        return True
#return empty list if right else return index of Box
def Box_checker(Board):
    Box_index = {}
    row = list()
    col = list()
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            for num in range(1, 10):
                if ((Board[x][y:y + 3] + Board[x + 1][y:y + 3] + Board[x + 2][y:y + 3]).count(num) != 1):
                    row.append(x)
                    col.append(y)

    return row,col
#return empty list if right else return index of col
def column__checker(Board):
        col_index = []
        for x in range(0,9):
            for y in range(0,8):
                for z in range(y+1,9):
                    if A[y][x]==A[z][x]:
                        col_index.append(x)
        return col_index
#return empty list if right else return index of row
def row_checker(Board):
    row_index = list()
    for x in range(0,9):
        for y in range(0,8):
            if Board[x][y] == Board[x][y+1]:
                row_index.append(x)

    return row_index



thread1 = pool.apply_async(Validation_of_num_of_column,args=(A,2))

if(thread1.get()==True):
    print("The NUM OF columns  IS RIGHT")
else:print("Error in column of",thread1.get())
