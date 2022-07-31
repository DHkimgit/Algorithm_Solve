array_1 = [1, 5, 4, 9, 0, 8, 7, 3, 2, 1, 4, 3]
array_2 = [2, 3, 2, 1, 7, 5, 7, 9, 8, 4, 5 ,1]
def quick_sort(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)
 
def quick_sort_py(array):
    #리스트가 하나 이상의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

quick_sort(array_1, 0, len(array_1) - 1)
print(array_1)
print(quick_sort_py(array_2))
