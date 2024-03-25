T = int(input())
result = []
def output(n, k, s):
    tmp = [k for x in range(n)]
    s.append(''.join(tmp))

for i in range(T):
    R, s = input().split()
    S = str(s)
    tmps = []
    for j in range(len(S)):
        output(int(R), S[j], tmps)
    result.append(''.join(tmps))

for i in result:
    print(i)
