N = str(input())
arr = [int(x) for x in N]
table = [0 for x in range(10)]

for num in arr:
    table[num] += 1

result = ((table[6] + table[9]) // 2) + ((table[6] + table[9]) % 2)

for i in range(10):
    if i != 6 and i != 9:
        result = max(result, table[i])
    
print(result)