import math
N = int(input())
lists = list(map(int, input().split()))
result = 0

def check_prime_number(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

for i in range(len(lists)):
    if check_prime_number(lists[i]):
        result += 1

print(result)