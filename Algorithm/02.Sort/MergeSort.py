def Merge(A: list, p: int, q: int, r: int):
    i = p
    j = q + 1
    t = 0
    # 임시 배열 생성
    tmp = [0] * (r - p + 1)
    
    # 두 부분 배열을 비교하며 병합
    while i <= q and j <= r:
        if A[i] < A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1
    
    # 왼쪽 부분 배열이 남은 경우
    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1
    
    # 오른쪽 부분 배열이 남은 경우
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
    
    # 임시 배열의 결과를 원래 배열에 복사
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1

def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    MergeSort(arr, 0, 6)
    print("정렬 후:", arr)