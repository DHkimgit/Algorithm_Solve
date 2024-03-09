N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)
result = 0

for i in range(len(scores)):
    scores[i] = (scores[i] / max_score) * 100
    result += scores[i]

print(result/N)