import sys

N = int(sys.stdin.readline())
input_int = list(map(str, sys.stdin.readline().split()))
M = int(input())

dp = [[0] * (N + 2) for _ in range(N + 1)] 

for i in range(1, N):
    dp[i][i] = 1

    if input_int[i - 1] == input_int[i]:
        dp[i-1][i+1] = 1

dp[N][N] = 1

for i in range(2, N): 
    for j in range(1, N - i + 1):
        if dp[j+1][i+j-1] == 1 and input_int[j-1] == input_int[i+j-1]:
            dp[j][j + i] = 1

output = ""

for i in range(M):
    S, E = map(int, input().split())

    if dp[S][E] == 1:
        output += "1\n"
    else:
        output += "0\n"

print(output.strip())

# def find_palindrome(S: int, E: int, input_int):
#     while S < E:
#         if input_int[S-1] != input_int[E-1]:
#             return False
#         else:
#             S += 1
#             E -= 1
#     return True

# t = [12, 31, 12, 48, 12, 31, 12]
# S = 1, E = 3, coca = 123112
# S = 1, E = 7, coca = 12 31 12 48 12 31 12
# S = 2, E = 6, coca = 31 12 48 12 31
# 1 7 2 6 3 5 44

# t2 = [12, 31, 12, 48, 48, 12, 31, 12]
# s = 1, E = 8, coca = 12 31 12 48 48 12, 31, 12
# S = 2, E = 7
# S = 3, E = 6
# S = 4, E = 5
# S = 5, E = 4

# for i in range(2, N+1):
#     for j in range(1, N + 1):
#         if i + j > N:
#             break
#         if input_int[j-1] == input_int[j+i-2] and dp[j+1][j+i-2]:
#             dp[j][j+i-1] == 1

    # print(S, E)
    # if dp[S][E] == 1:
    #     result_list.append('1')
    #     continue

    # elif dp[S-1][E+1] == 1:
    #     dp[S][E] = 1
    #     result_list.append('1')
    #     continue

    # if find_palindrome(S, E, input_int):
    #     dp[S][E] = 1
    #     result_list.append('1')
    # else:
    #     result_list.append('0')


