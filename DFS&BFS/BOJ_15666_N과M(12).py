N,M = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()

result = [0] * M

def backtracking(k, idx):
    if k == M:
        for i in range(M):
            print(result[i], end=' ')
        print()
        return

    temp = 0
    for i in range(idx, N):
        if temp != lists[i]:
            result[k] = lists[i]
            temp = lists[i]
            backtracking(k+1, i)

backtracking(0, 0)