a = int(input())
lst = ['A', 'B', 'C', 'D', 'F']
start = 100
end = 90
for i in range(5):
    if a <= 59:
        print("F")
        break
    if a >= end and a <= start:
        print(lst[i])
        break
    start -= 10
    end -= 10