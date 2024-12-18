import math
N = int(input())

array = []
pl = []

end = 0
interval_sum = 0
counter = 0

arr = [True for i in range(N + 1)] # 처음엔 모든 수가 소수(TRUE)인것으로 초기화

for i in range(2, int(math.sqrt(N)) + 1): #에라토스테네스 알고리즘 수행. 2부터 n의 제곱근까지 
    if arr[i] == True: # 만약 배열 안의 수가 소수라면
        j = 2 # 배수를 제거하는데 사용하는 변수
        while i*j <= N: # 배수가 N에 도달할때까지 j값을 증가
            arr[i * j] = False # 배수에 해당하는 수는 소수에서 제외
            j += 1
    
for i in range(2, N+1): # 주어진 범위 안에서 소수(True)인 i값만 새로운 배열 pl에 할당
    if arr[i]:
        pl.append(i)

M = len(pl)        

for start in range(M): # 투포인터 알고리즘
    while interval_sum < N and end < M:
        interval_sum = interval_sum + pl[end]
        end = end + 1
    if interval_sum == N:
        counter += 1
    interval_sum = interval_sum - pl[start]

print(counter)