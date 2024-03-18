table = [[0 for x in range(100)] for x in range(100)]

n = int(input())
result = 0

for i in range(n):
    a, b = map(int, input().split())
    for j in range(b, b+10):
        for k in range(a, a+10):
            if table[j][k] == 0:
                result += 1
            table[j][k] = 1
    
print(result)