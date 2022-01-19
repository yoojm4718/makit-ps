#공항 방문객 수 구하기

visitor = [4, 7, 2, 9, 3]

#가장 많은 방문객 수 구하기
max1 = 0
for x in visitor:
    if x > max1:
        max1 = x

#max1을 제외한 새로운 리스트 만들기
new_visitor = []
for x in visitor:
    if x != max1:
        new_visitor.append(x)

#새로운 리스트에서 가장 많은 방문객 수 구하기
max2 = 0
for x in new_visitor:
    if x > max2:
        max2 = x

#결과값 구하기
result = max1 - max2
print("결과 :"+str(result))
        
        
