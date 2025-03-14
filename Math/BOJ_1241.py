import math
N = int(input())
table = []
max_val = 0

for i in range(N):
    val = int(input())
    if val > max_val:
        max_val = val
    table.append(val)

cnt = [0 for x in range(max_val + 1)]

for i in table:
    cnt[i] += 1

result = [0 for _ in range(max_val + 1)]

for i in table:
    if result[i] != 0:
        continue
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if j * j != i:
                result[i] += cnt[j] + cnt[i//j]
            else:
                result[i] += cnt[j]
for i in table:
    print(result[i] - 1)

    # if cnt[i] != 0:
    #     result = 0
    #     yaks = yaksu(i)
    #     for j in yaks:
    #         result += cnt[j]
    #     print(result - 1)

# O(n^2) 이므로 시간초과 발생
# N = int(input())
# table = []
# result = [0 for x in range(N)]
# for i in range(N):
#     val = int(input())
#     table.append(val)

# for i in range(N):
#     for j in range(N):
#         if j != i:
#             if table[i] % table[j] == 0:
#                 result[i] += 1
            
# for i in range(N):
#     print(result[i])

