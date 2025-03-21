def switching_merge(p, q, r, C, D):
    i = p
    j = q + 1
    t = p
    
    # 두 부분 배열을 비교하며 병합
    while i <= q and j <= r:
        if C[i] <= C[j]:
            D[t] = C[i]
            t += 1
            i += 1
        else:
            D[t] = C[j]
            t += 1
            j += 1
    
    # 왼쪽 부분 배열이 남은 경우
    while i <= q:
        D[t] = C[i]
        t += 1
        i += 1
    
    # 오른쪽 부분 배열이 남은 경우
    while j <= r:
        D[t] = C[j]
        t += 1
        j += 1

def swt_ms(p, r, A, B):
    if p < r:
        q = (p + r) // 2
        swt_ms(p, q, B, A)  # A와 B의 역할을 교대
        swt_ms(q + 1, r, B, A)  # A와 B의 역할을 교대
        switching_merge(p, q, r, B, A)

def switching_mergesort(A, n):
    # 보조 배열 B 생성 및 초기화
    B = [0] * n
    for i in range(n):
        B[i] = A[i]
    
    # 스위칭 병합 정렬 시작
    swt_ms(0, n-1, A, B)

if __name__ == "__main__":
    arr = [64, 34, 25, 90, 22, 12, 11]
    n = len(arr)
    
    print("정렬 전:", arr)
    switching_mergesort(arr, 7)
    print("정렬 후:", arr)