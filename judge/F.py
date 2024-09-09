N = int(input())

low_range = []
high_range = []

for i in range(N):
    n, m = map(int, input().split())
    low_range.append(n)
    high_range.append(m)

print(max(low_range) - min(high_range))

# 6 - 7

# 5
# 2 5 => 5
# 12 18 => 14
# 3 6 => 5
# 1 8 => 5
# 14 16 => 14

# 5
# 2 5
# 12 18
# 3 6
# 1 8
# 14 16

