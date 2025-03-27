import random
import time

def InsertionSort(A: list, n: int):
    for i in range(1, n):
        newItem = A[i]
        j = i - 1
        while j >= 0 and newItem < A[j]:
            A[j +1] = A[j]
            j -= 1
        A[j + 1] = newItem

if __name__ =="__main__":
    arr = []
    for i in range(10000):
        arr.append(random.randint(1, 100000))
    print("정렬 전 배열 (범위 인덱스 0 ~ 50)")
    print(arr[0:50])
    print("정렬 시작")
    start = time.time()
    InsertionSort(arr, 10000)
    end = time.time()
    sec = end - start
    print("정렬 후 배열 (범위 인덱스 0 ~ 50)")
    print(arr[0:50])
    print("소요 시간:", str(sec) +' 초')