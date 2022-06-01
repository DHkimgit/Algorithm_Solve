n = int(input())
arr = list(map(int, input().split()))


int_sum = 0
sum = 0

for start in range(n):
    for end in range(start + 1, n):
        int_sum = 0
        for i in range(start, end):
            int_sum = int_sum + arr[i]
        if int_sum > sum:
            sum = int_sum
        else:
            continue            
            
print(sum)    