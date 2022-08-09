def solution(arr):
    answer = 0
    sum_array = 0
    for i in range(len(arr)):
        sum_array += arr[i]
    answer = sum_array / len(arr)
    return answer