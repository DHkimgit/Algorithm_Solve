N = int(input())
k = list(map(int, input().split()))

honey = []
k_sum = 0

for i in range(len(k)):
    k_sum += k[i]
    honey.append(k_sum)

total_sum = 0
# 꿀통 벌 벌 - 벌 한마리 오른쪽 끝에 고정
for i in range(1, N-1):
    bee_a = honey[i-1]
    bee_b = honey[N-2] - k[i]
    total_sum = max(total_sum, bee_a + bee_b)

# 벌 벌 꿀통 = 벌 한마리 왼쪽 끝에 고정
for i in range(1, N-1):
    bee_a = honey[N-1] - honey[i]
    bee_b = honey[N-1] - k[i] - honey[0]
    total_sum = max(total_sum, bee_a + bee_b)

# 벌 꿀통 벌 - 꿀통이 움직임, 벌 두마리 양쪽 고정
for i in range(1, N-1):
    bee_a = honey[i] - honey[0]
    bee_b = honey[N-2] - honey[i - 1]
    total_sum = max(total_sum, bee_a + bee_b)

print(total_sum)
