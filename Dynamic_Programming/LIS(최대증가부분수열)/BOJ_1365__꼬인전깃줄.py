N = int(input())

k = list(map(int, input().split()))
end_storage = []

def binary_search(k, start, end, num):
    while start < end:
        mid = (start + end) // 2
        if k[mid] < num:
            start = mid + 1
        else:
            end = mid
    
    return end

end_storage.append(k[0])

for num in k:
    start, end = 0, len(end_storage)
    if num > end_storage[-1]:
        end_storage.append(num)
    
    pos = binary_search(end_storage, start, end, num)
    end_storage[pos] = num

print(len(k) - len(end_storage))
