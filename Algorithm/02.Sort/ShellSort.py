def stepInsertionSort(A, k, h, n):
    for i in range(k + h, n, h):  # k+h부터 n-1까지 h 간격으로
        newItem = A[i]
        j = i - h
        while j >= 0 and newItem < A[j]:
            A[j + h] = A[j]
            j -= h
        A[j + h] = newItem

def shellSort(A):
    n = len(A)
    # 갭 수열 정의 (예: Hibbard's sequence)
    # h = 2^k - 1: 1, 3, 7, 15, 31, ...
    gaps = []
    h = 1
    while h < n:
        gaps.append(h)
        h = 2 * h + 1
    
    # 큰 간격부터 시작하여 간격 1까지 수행
    for h in reversed(gaps):
        # 각 부분 리스트에 대해 삽입 정렬 수행
        for k in range(h):
            stepInsertionSort(A, k, h, n)

if __name__ == "__main__":
    # 테스트용 배열
    arr = [64, 34, 25, 90, 22, 12, 11]
    print("정렬 전:", arr)
    
    shellSort(arr)
    print("정렬 후:", arr)