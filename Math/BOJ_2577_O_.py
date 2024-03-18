a = int(input())
b = int(input())
c = int(input())

result = [0 for x in range(10)]

T = str(a*b*c)

for i in range(len(T)):
    result[int(T[i])] += 1

for x in result:
    print(x)
