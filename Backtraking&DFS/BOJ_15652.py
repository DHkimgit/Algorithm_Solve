import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def backtracking(x):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(x, N + 1):
        result.append(i)
        backtracking(i)
        result.pop()

backtracking(1)