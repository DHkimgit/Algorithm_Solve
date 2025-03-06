n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n - 1
result = 0

while left < right:
    if arr[left] + arr[right] == x:
        result += 1
        right -= 1
    elif arr[left] + arr[right] > x:
        right -= 1
    else:
        left += 1

print(result)


# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())
# result = 0

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         if arr[j] + arr[i] == x:
#             result += 1

# print(result)