n = int(input())
rt = []
maxv = -1000000000
for i in range(n):
    tmp = int(input())
    rt.append(tmp)
    tmp = 0

minv = rt[0]

for j in range(1, n):
    maxv = max(maxv, rt[j] - minv)
    minv = min(minv, rt[j])

print(maxv)


