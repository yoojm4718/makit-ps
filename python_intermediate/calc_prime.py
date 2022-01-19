def calc_prime(n):
    check = [0]*101

    for i in range(2,11):
        if check[i] == 0:
            for x in range(i*2, 101, i):
                check[x] = 1
    for i in range(2, 101):
        if check[i] == 0:
            print(i, end=' ')

print("에라토스테네스의 체 (n=100)")
calc_prime(100)



