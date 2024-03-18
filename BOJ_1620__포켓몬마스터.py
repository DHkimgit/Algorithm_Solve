N, M = map(int, input().split())

dogam = []

question = []

for i in range(N):
    dogam.append(str(input()))

for i in range(M):
    tmp = input()
    if tmp.isdigit():
        question.append(int(tmp))
    else:
        question.append(tmp)

for i in range(M):
    if str(type(question[i])) == "<class 'int'>":
        print(dogam[question[i] - 1])
    else:
        print(dogam.index(question[i]) + 1)