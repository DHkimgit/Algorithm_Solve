def binary_search(target, array, start, end):
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(target, array, start, mid - 1)
    else:
        return binary_search(target, array, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(target, array, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)