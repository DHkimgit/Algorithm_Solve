import heapq

T = int(input())

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        if left == len(tails): # 현재 원소가 `tails` 배열의 모든 원소보다 클때
            tails.append(num)
        else:
            tails[left] = num
    return len(tails)

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N
    print(dp)

    
    for i in range(1, N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))
    print(lengthOfLIS(arr))

