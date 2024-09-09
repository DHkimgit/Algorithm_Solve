k = int(input())
result = 0
prime_number = [i for i in range(1, k + 1)]
exp = [0 for i in range(1, k + 1)]
exp[0] = 1

for i in range(2, k):
    t = 2
    while i * t <= k:
        exp[i*t - 1] = 1
        t += 1

for i in range(len(exp)):
    if exp[i] == 0:
        result += 1
    if i == k:
        break
print(result)
