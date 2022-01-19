#두 자연수 n부터 m까지의 합 구하기
#for문 사용

def func(k):
    sum = 0
    for x in range(k+1):
        sum += x
    return sum

n = int(input("n을 입력 :"))
m = int(input("m을 입력 :"))
sum_to_n = func(n-1)
sum_to_m = func(m)
answer = sum_to_m - sum_to_n

print(str(n)+"부터 "+str(m)+"까지의 합은"+str(answer)+"입니다.")


