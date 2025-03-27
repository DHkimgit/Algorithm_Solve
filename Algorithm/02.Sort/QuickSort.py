import random
import time

def partition(A: list, p: int, r: int):
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

if __name__ =="__main__":
    arr = []
    for i in range(10000):
        arr.append(random.randint(1, 100000))
    print("정렬 전 배열 (범위 인덱스 0 ~ 50)")
    print(arr[0:50])
    print("정렬 시작")
    start = time.time()
    quickSort(arr, 0, 9999)
    end = time.time()
    sec = end - start
    print("정렬 후 배열 (범위 인덱스 0 ~ 50)")
    print(arr[0:50])
    print("소요 시간:", str(sec) +' 초')