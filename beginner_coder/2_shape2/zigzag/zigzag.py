n = int(input())

board = [[0 for i in range(n)] for j in range(n)]

def make_zigzag():
    x = 0
    y = 0
    for i in range(n * n):
        cur = i + 1
        board[x][y] = cur
        # print(f"{x} {y} {board[x][y]} {cur}")
        if(x == n - 1):
            if(n % 2 == 0):
                if(y % 2 == 0):
                    x -= 1
                    y += 1
                else:
                    y += 1
            else:
                if(y % 2 == 0):
                    y += 1
                else:
                    x -= 1
                    y += 1
        elif(y == 0):
            if(x % 2 == 0):
                x += 1
            else:
                x -= 1
                y += 1
        elif(y == n - 1):
            if(n % 2 == 0):
                if(x % 2 == 0):
                    x += 1
                else:
                    x += 1
                    y -= 1
            else:
                if(x % 2 == 0):
                    x += 1
                    y -= 1
                else:
                    x += 1
        elif(x == 0):
            if(y % 2 == 0):
                x += 1
                y -= 1
            else:
                y += 1
        else:
            if((x + y) % 2 == 0):
                x += 1
                y -= 1
            else:
                x -= 1
                y += 1

make_zigzag()

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()