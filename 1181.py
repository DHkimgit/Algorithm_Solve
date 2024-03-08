N = int(input())

lists = []

for _ in range(N):
    word = str(input())
    len_word = len(word)
    lists.append((word, len_word))

result = list(set(lists))

result.sort(key = lambda x: (x[1], x[0]))

for i in range(len(result)):
    print(result[i][0])
