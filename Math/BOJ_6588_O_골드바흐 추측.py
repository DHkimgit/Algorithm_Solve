import math
# 수 0이 나올 때 까지 입력 받기
lists = []

while True:
    k = int(input())
    if k == 0:
        break
    lists.append(k)
    
#에라토스테네스의 체
n = max(lists)
table = [True] * (n+2)

for i in range(2,n+1):
    if table[i] == True:
        for j in range(2 * i, n + 2, i):
            table[j] = False

# 합 판정
def printNum(K):
    for i in range(2, len(table)):
        if table[i] == True and table[K-i] == True:
            print(f"{K} = {i} + {K - i}")
            break

for j in range(len(lists)):
    printNum(lists[j])
