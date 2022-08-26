N = int(input())
array = list(map(int, input().split()))
v = int(input())
result = 0
for i in range(len(array)):
    if array[i] == v:
        result += 1

print(result)
