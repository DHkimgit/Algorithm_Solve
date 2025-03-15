import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

votes = [0] * N
junghu = 0
other_sum = 0
max_val = 0

for _ in range(Q):
    a, b, c = map(int, input().split())
    if a == 1:
        if c == N + 1:
            junghu += b
        else:
            votes[c - 1] += b
            other_sum += b
            max_val = max(max_val, votes[c - 1])
    else:
        new_junghu = junghu + b
        print("YES" if (new_junghu > max_val) and (other_sum + c <= N * (new_junghu - 1)) else "NO")

# result =dict()

# for i in range(1, N+2):
#     result[i] = 0

# def vote(result: dict, candidate: int, count: int):
#     result[candidate] += count

# def calc_current_loser_except_junghu(dicts: dict) -> int:
#     min_votes = 999999
#     result = 0
#     for key in dicts:
#         if key != N+1 and dicts[key] < min_votes:
#             min_votes = dicts[key]
#             result = key
#     return result

# def counting(result: dict, junghu: int, other: int):
#     current_loser = result[calc_current_loser_except_junghu(result)]
#     current_junghu = result[N+1]

#     if current_loser + other >= current_junghu + junghu:
#         print('NO')
#     else:
#         print('YES')

# for i in range(Q):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         vote(result, c, b)
#     else:
#         counting(result, b, c)


    





