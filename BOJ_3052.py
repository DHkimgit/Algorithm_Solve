result = []
for _ in range(10):
    A = int(input())
    if (A % 42) not in result:
        result.append(A % 42)
    else:
        pass
print(len(result))