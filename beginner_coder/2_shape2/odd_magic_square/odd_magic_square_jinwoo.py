def solution(a):
    arr=[[0 for _ in range(a)]for _ in range(a)]
    y=0
    x=a//2
    c=1
    arr[y][x]=c
    c+=1
    while True:
        if arr[y-1][x-1]==0:
            y-=1
            x-=1
            if x==-1:
                x=a-1
            if y==-1:
                y=a-1
        else:
            if y+1==a:
                y=0
            else:
                y+=1
            if arr[y][x]!=0:
                break
        arr[y][x]=c
        c+=1   
    return arr
num=int(input())
arr=solution(num)
for i in range(num):
    if i!=0:
        print()
    for j in range(num):
        print(arr[i][j],end=' ')