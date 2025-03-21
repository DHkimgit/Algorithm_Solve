def bubbleSort(A: list, n: int):
    for last in range(n-1, 0, -1):
        sorted_flag = True
        for i in range(0, last):
            if A[i] > A[i + 1]:
                tmp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = tmp
                sorted_flag = False
        if sorted_flag == True:
            return

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    bubbleSort(arr, n)
    print("정렬 후:", arr)