result = []

while True:
    lengths = list(map(int, input().split()))
    if lengths[0] == 0 and lengths[1] == 0 and lengths[2] == 0:
        break
    lengths.sort()
    if lengths[2] * lengths[2] == lengths[0] * lengths[0] + lengths[1] * lengths[1]:
        result.append("right")
    else:
        result.append("wrong")
    
for i in range(len(result)):
    print(result[i])
