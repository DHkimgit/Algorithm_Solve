total_amount = int(input())
total_purchased = int(input())

result = 0

for i in range(total_purchased):
    a, b = map(int, input().split())
    result += a*b

if result == total_amount:
    print('Yes')
else:
    print('No')
