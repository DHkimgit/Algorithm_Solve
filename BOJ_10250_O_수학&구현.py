test_case = int(input())
result = []
for i in range(test_case):
    guest = 0
    tmp = []
    H, W, N = map(int, input().split())
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            guest += 1
            if guest == N:
                tmp.append(i)
                tmp.append(j)
    result.append(tmp[1] * 100 + tmp[0])

for i in range(len(result)):
    print(result[i])
