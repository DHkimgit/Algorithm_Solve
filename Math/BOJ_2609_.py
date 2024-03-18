a, b = map(int, input().split())
K = min(a, b) 
T = max(a, b) 
result_max = [1]
result_min = 0
for i in range(2, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        result_max.append(i)

for i in range(1, K+1):
    if (T * i) % K == 0:
        result_min = T*i
        break
if a != b:
    print(max(result_max))
else:
    print(a)
print(result_min)
