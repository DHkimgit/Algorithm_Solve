test_case = int(input())
result = []
for _ in range(test_case):
    k = int(input())
    n = int(input())
    floor = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor[j] = floor[j] + floor[j - 1]
    result.append(floor[-1])

for i in range(test_case):
    print(result[i])
