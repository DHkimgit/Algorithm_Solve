N = int(input())

K = list(map(int, input().split()))

end_storage = []
end_storage.append(K[0])

def binary_search(K, left, right, num):
    while left < right:
        mid = (left + right) // 2
        if num > K[mid]:
            left = mid + 1
        else:
            right = mid
        
    return right

for num in K:
    left, right = 0, len(end_storage)
    if num > end_storage[-1]:
        end_storage.append(num)
    
    pos = binary_search(end_storage, left, right, num)
    end_storage[pos] = num

print(len(end_storage))