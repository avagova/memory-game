import random as rn
open_ = []
board = []


def print_board(n, m):
    print()
    global board
    global open_
    elem = 0
    for i in range(0, n):
        for j in range(0, m):
            res = "*"
            if tuple([i, j]) in open_:
                res = board[i*m+j]
            print(res, end='\t')
            elem += 1
        print("")


n = m = 1
while n % 2 and m % 2:
    n = int(input("input rows size:\t"))
    m = int(input("input colums size:\t"))
len_ = n*m
board = [0] * len_
free_ind = [i for i in range(0, len_)]
while len(free_ind) != 0:
    ind = rn.randint(1, len(free_ind)-1)
    board[free_ind[ind]] = board[free_ind[0]] = rn.randint(0, 100)
    del free_ind[ind]
    del free_ind[0]
print()
print_board(n, m)
free_ind = [i for i in range(0, len_)]
while len(open_) != len_:
    cord1 = eval(input("1st elem cordinates: "))
    if (cord1[0] > n-1 or cord1[0] < 0) or (cord1[1] > m-1 or cord1[1] < 0):
        print("wrong cordinates!")
        continue
    cord2 = eval(input("2nd elem cordinates: "))
    if (cord2[0] > n-1 or cord2[0] < 0) or (cord2[1] > m-1 or cord2[1] < 0):
        print("wrong cordinates!")
        continue
    if cord1 in open_:
        print("1st element already opened")
        continue
    if cord2 in open_:
        print("2nd element already opened")
        continue
    open_.append(cord1)
    open_.append(cord2)
    print_board(n, m)
    if board[cord1[0] * m+cord1[1]] != board[cord2[0] * m+cord2[1]]:
        open_.remove(cord1)
        open_.remove(cord2)
        
print("Yaaaa, you won!")
