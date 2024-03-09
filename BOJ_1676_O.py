import math

N = int(input())

fact = str(math.factorial(N))

fact_r = fact[::-1]

result = 0

for i in range(len(fact_r)):
    if fact_r[i] == '0':
        result += 1
    else:
        break

print(result)
