t = int(input())

for i in range(t):
    answer = input()
    answer_len = len(answer)
    arr = []
    
    for k in range(answer_len):
        arr.append(answer[k])

    if arr[::-1] == arr:
        print("PRETTY")
    else:
        print("CUTE")





