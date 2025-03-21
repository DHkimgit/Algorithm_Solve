def partition(A, p, r):
    x = A[r]  # 기준원소
    i = p - 1  # 1구역의 끝 지점
    
    # j는 3구역의 시작 지점
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i] # i값 증가 후 A[i]와 A[j] 교환
    
    # 기준 원소와 2구역 첫 원소 교환
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    quickSort(arr, 0, 6)
    print("정렬 후:", arr)