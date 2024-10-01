import sys
def input(): return sys.stdin.readline().rstrip()

string = list(input())
k = int(input())
temp = []

for _ in range(k):
    order = str(input())

    if order == "B":
        if string:
            string.pop()
    
    elif order[0] == "P":
        string.append(order[2])
    
    elif order == "L":
        if string:
            temp.append(string.pop())
    
    else:
        if temp:
            string.append(temp.pop())

while temp:
    string.append(temp.pop())

print(''.join(string))