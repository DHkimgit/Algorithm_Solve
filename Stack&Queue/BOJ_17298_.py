N = int(input())
array = list(map(int, input().split()))
result = [-1] * N
stack = [0]


for i in range(1, N):
    while stack and array[i] > array[stack[-1]]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)
