def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
target = list(map(int, input().split()))

for i in range(M):
    result = binary_search(array, target[i], 0 , N - 1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
