N  = int(input())
lists = list(input().split(' '))
print(lists)
stack = []
result = []
run = 0
tmp = 0
for i in range(N-1, 0):
    while(lists[i]<tmp):
        tmp = lists.pop()
        stack.append(tmp)
        run += 1
    result.append(N-run+1)
    for j in range(len(stack)-1, 0):
        lists.append(stack[j])
    for k in range(len(stack)):
        stack.pop()
    lists.pop()

print(result.reverse())
#https://www.acmicpc.net/problem/2493
    
