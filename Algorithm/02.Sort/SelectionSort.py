def theLargest(A, last):
    largest = 0
    for i in range(1, last + 1):
        if A[i] > A[largest]:
            largest = i
    return largest

def selectionSort(A, n):
    for last in range(n-1, 0, -1):
        k = theLargest(A, last)
        # swap
        tmp = A[k]
        A[k] = A[last]
        A[last] = tmp

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)
    
    print("정렬 전:", arr)
    selectionSort(arr, n)
    print("정렬 후:", arr)