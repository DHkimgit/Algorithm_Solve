N = int(input())
num = [0] + list(map(int, input().split()))
print(num)  # num 리스트를 0을 포함하여 초기화

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1  # 한 자리 수는 무조건 팰린드롬

    # 두 자리가 같은 경우들 기록
    if i != 1 and num[i - 1] == num[i]:
        dp[i - 1][i] = 1

for i in range(2, N):
    for j in range(1, N - i + 1):
        if num[j] == num[i + j] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

M = int(input())

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s][e])