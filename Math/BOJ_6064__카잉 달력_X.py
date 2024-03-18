T = int(input())
result = []


for i in range(T):
    M, N, x, y = map(int, input().split())
    storage = []
    X = 1
    Y = 1
    while X!=M or Y!=N:
        storage.append((X, Y))
        X += 1
        Y += 1
        if X > M:
            X = 1
        if Y > N:
            Y = 1
    before = len(result)
    for i in range(len(storage)):
        if storage[i][0] == x and storage[i][1] == y:
            result.append(i + 1)
            continue
    after = len(result)
    
    if before == after:
        result.append(-1)
    

print(result)
