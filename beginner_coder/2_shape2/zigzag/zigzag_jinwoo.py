def solution(a):
    arr = [[0 for j in range(a)] for i in range(a)]
    if a%2==1:
        x1=0
        y1=a-1
    elif a%2==0:
        x1=a-1
        y1=0
    x=0
    y=0
    c1=2
    arr[0][0]=1
    if a==1:
        return 1
    y+=1
    arr[y][x]=c1
    c1+=1
    count=0
    while True:
        while True:
            x+=1
            y-=1
            arr[y][x]=c1
            c1+=1
            if y==0 or x==a-1:
                break

        if x==a-1 and y==a-1:
                break
        if x==x1 and y==y1:
            count +=1
        if count==0:
            x+=1
        elif count==1:
            y+=1
        if x==x1 and y==y1:
            count +=1
        arr[y][x]=c1
        c1+=1
        if x==a-1 and y==a-1:
            break
        while True:
            x-=1
            y+=1
            arr[y][x]=c1
            c1+=1
            if x==0 or y==a-1:
                break
        if x==a-1 and y==a-1:
            break
        if x==x1 and y==y1:
            count +=1
        if count==0:
            y+=1
        elif count==1:
            x+=1
        if x==x1 and y==y1:
            count +=1
        arr[y][x]=c1
        c1+=1
        if x==a-1 and y==a-1:
            break
    return arr

a=int(input())
arr=solution(a)

if arr==1:
    print(1)
else:
    for i in range(a):
        if i!=0:
            print()
        for j in range(a):
            print(arr[i][j],end=' ')
            
# 일반화 필요성