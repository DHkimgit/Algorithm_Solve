def insertionSort_Asc(arr, first, last, gap):
    i = first + gap
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos - gap] >val:
            arr[pos] = arr[pos - gap]
            pos -= gap
        arr[pos] = val
        i += gap

def shellSort_Asc(arr):
    n = len(arr)
    h = n//2
    while h > 0:
        for i in range(0, h):
            insertionSort_Asc(arr, i, n-1, h)
        h //= 2
    return arr

from random import randint

lst = [randint(1, 101) for i in range(8)]
print(shellSort_Asc(lst))