def InsertionSort(A: list, n: int):
    for i in range(1, n):
        newItem = A[i]
        j = i - 1
        while j >= 0 and newItem < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = newItem

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    InsertionSort(arr, n)
    print("정렬 후:", arr)