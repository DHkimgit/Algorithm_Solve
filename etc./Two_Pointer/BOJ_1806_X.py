N, S = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
interval_sum = 0
ls = []
count = 0
sum_arr = 0

for i in range(N):
    sum_arr += arr[i]

if sum_arr < S:
    print(0)

else :
    for start in range(N):
        while interval_sum < S and end < N:
            interval_sum = interval_sum + arr[end]
            end = end + 1
        if interval_sum >= S:
            count += 1
            ls.append(end - start + 1)
    
        interval_sum = interval_sum - arr[start]
    
    print(min(ls))
