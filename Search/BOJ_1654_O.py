K, N = map(int, input().split())
array = []

for i in range(K):
    array.append(int(input()))

def calc_N(array, div):
    result = 0
    for i in range(len(array)):
        result += int(array[i]) // div
    return result

def binary_search(array, target: int, start: int, end: int):
    while (start <= end):
        mid = (start + end) // 2
        if calc_N(array, mid) >= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

result = binary_search(array, int(N), int(1), int(max(array)))

print(result)
