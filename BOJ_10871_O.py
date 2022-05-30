n, x = map(int, input().split())
nl = list(map(int, input().split()))

arr = []

for i in range(0, n):
    if nl[i] < x:
        arr.append(nl[i])
    else:
        continue

for i in range(len(arr)):
    print(arr[i], end=' ')
