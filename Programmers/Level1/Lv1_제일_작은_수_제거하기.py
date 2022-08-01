array = list(map(int, input().split()))

def solution(arr):
    standered = 100000000
    pointer = 0
    for i in range(len(arr)):
        if arr[i] < standered:
            standered = arr[i]
            pointer = i
    arr.pop(pointer)
    if not arr:
        return [-1]
    else:
        return arr

print(solution(array))