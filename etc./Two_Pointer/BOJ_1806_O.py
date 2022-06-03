N, S = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
interval_sum = 0
ls = []
sum_arr = 0

for i in range(N):
    sum_arr += arr[i]

if sum_arr < S:
    print(0)

elif S == 0:
    print(1)

else :
    for start in range(N):
        if interval_sum >= S:
                ls.append(end - start) 
        while interval_sum < S and end < N:
            interval_sum = interval_sum + arr[end]
            if interval_sum >= S:
                ls.append(end - start + 1)
            end = end + 1
        interval_sum = interval_sum - arr[start]
    
    print(min(ls))
"""
N = 10, S = 100일때 배열이 98 1 1 1 50 50 1 1 1 98 인 경우 중간 start = 4, end = 5 일때 최솟값이 나와야 한다. 따라서 2가 답이어야 하는데


"""