n = int(input())
nl = list(map(int, input().split()))

start = 0
end = 0
sum_t = 0
sum = 0
for start in range(n):
    for end in range(n):
        for i in range(start, end + 1):
            sum_t = sum_t + nl[i]
        if sum_t > sum:
            sum = sum_t
            
            
print(sum)
