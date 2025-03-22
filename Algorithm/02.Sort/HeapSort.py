def percolateDown(A, k, n):
    child = 2 * k + 1  # 왼쪽 자식
    right = 2 * k + 2  # 오른쪽 자식
    
    if child <= n - 1:  # 자식이 있는 경우
        # 오른쪽 자식이 있고, 왼쪽 자식보다 더 큰 경우
        if right <= n - 1 and A[child] < A[right]:
            child = right
        
        # 현재 노드가 선택된 자식보다 작은 경우
        if A[k] < A[child]:
            # 교환
            A[k], A[child] = A[child], A[k]
            # 재귀적으로 자식 노드에 대해 percolateDown 수행
            percolateDown(A, child, n)

def buildHeap(A):
    n = len(A)
    # 수도코드와 동일하게 (n-2)/2부터 시작하여 0까지 감소
    for i in range((n-2)//2, -1, -1):
        percolateDown(A, i, n)

def deleteMax(A, n):
    max_val = A[0]  # 최대값 저장
    A[0] = A[n-1]  # 마지막 원소를 루트로 이동
    n -= 1  # 크기 감소
    percolateDown(A, 0, n)  # 루트에서 시작하여 percolateDown 수행
    return max_val

def heapSort(A):
    n = len(A)
    # 초기 힙 생성
    buildHeap(A)
    
    # 힙에서 최대값을 차례로 삭제하여 배열의 뒤쪽부터 저장
    for i in range(n-1, 0, -1):  # n-1부터 1까지 감소
        A[i] = deleteMax(A, i+1)

# 테스트
if __name__ == "__main__":
    # 테스트용 배열
    arr = [64, 34, 25, 90, 22, 12, 11]
    print("정렬 전:", arr)
    
    heapSort(arr)
    print("정렬 후:", arr)