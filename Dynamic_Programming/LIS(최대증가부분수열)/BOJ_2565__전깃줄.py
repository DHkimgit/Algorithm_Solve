N = int(input())

data = []
K = []
end_storage = []

for i in range(N):
    a, b = map(int, input().split())

    data.append((a, b))

data.sort()

for i in range(N):
    K.append(data[i][1])

def binary_search(K, left, right, num):
    while left < right:
        mid = (left + right) // 2
        if num > K[mid]:
            left = mid + 1
        else:
            right = mid
        
    return right

end_storage.append(K[0])

for num in K:
    left, right = 0, len(end_storage)
    if num > end_storage[-1]:
        end_storage.append(num)
    
    pos = binary_search(end_storage, left, right, num)
    end_storage[pos] = num

print(N - len(end_storage))