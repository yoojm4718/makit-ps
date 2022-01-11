n = int(input())

board = [[0 for i in range(n)] for j in range(n)]

def make_magic_square():
    x = 0
    y = n // 2
    for i in range(n * n):
        cur = i + 1
        board[x][y] = cur;
        if(cur % n == 0):
            x += 1
        else:
            x = (x - 1) % n
            y = (y - 1) % n

make_magic_square()

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()