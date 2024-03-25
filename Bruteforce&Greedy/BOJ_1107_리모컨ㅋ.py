def check_broken(num):
    if num == 0:
        if broken[num] == True:
            return -1
        return 1
    
    length = 0
    while num > 0:
        if broken[num % 10] == True:
            return -1
        length += 1
        num = num // 10
    return length

N = int(input())
M = int(input())

if M == 0:
    print(len(str(N)))

else:   
    broke = list(map(int, input().split()))
    broke.sort()
    broken = [False for x in range(10)]

    for button in broke:
            broken[button] = True

    if N == 100:
        print(0)

    else:
        result = abs(100 - N)
        for i in range(0, 1000000):
            count = check_broken(i)
            if count > 0:
                count += abs(N - i)
                if count == 23:
                    print(i)
                    print("asdasd")
                result = min(result, count)
        print(result)
