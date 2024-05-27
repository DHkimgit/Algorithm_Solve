from itertools import combinations
N, C = map(int, input().split())
alpha = list(map(str, input().split()))

vow = [] #모음
cons = [] # 자음
result = []

for i in range(len(alpha)):
    if alpha[i] == 'a' or alpha[i] == 'e' or alpha[i] == 'i' or alpha[i] == 'o' or alpha[i] == 'u':
        vow.append(alpha[i])
    else:
        cons.append(alpha[i])

vmax = len(vow)

if len(vow) >= 1 and len(cons) >= 2:
    for i in range(1, vmax + 1):
        v = list(combinations(vow, i))
        c = list(combinations(cons, N-i))

        for j in range(len(v)):
            for k in range(len(c)):
                sorted_combination = sorted(list(v[j]) + list(c[k]))
                result.append(''.join(sorted_combination))

    result.sort()

    for i in range(len(result)):
        print(result[i])

else:
    pass