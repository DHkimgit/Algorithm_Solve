n, m = map(int, input().split())
score = list(map(int, input().split()))

score.sort()

print(score[m-1])