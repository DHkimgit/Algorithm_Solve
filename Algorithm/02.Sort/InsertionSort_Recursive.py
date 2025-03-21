def InsertionSort(A, n):
    # 기저 조건: n이 1 이하면 이미 정렬된 상태
    if n > 1:
        # 먼저 n-1개 원소를 정렬
        InsertionSort(A, n-1)
        
        # A[n-1]을 정렬된 배열의 적절한 위치에 삽입
        last = A[n-1]
        j = n-2
        
        # last보다 큰 원소들을 오른쪽으로 이동
        while j >= 0 and A[j] > last:
            A[j+1] = A[j]
            j -= 1
        
        # 적절한 위치에 last 삽입
        A[j+1] = last

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    InsertionSort(arr, n)
    print("정렬 후:", arr)