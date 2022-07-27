array = []
N = int(input())
order_list = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(str, input().split()))
    order_list[i].append(tmp)

print(order_list)

def size(array):
    return len(array)

def empty(array):
    result = 0
    if empty(array):
        result = 1
    return result

def push_back(array, N):
    array.append(N)

def push_front(array, N):
    array.insert(0, N)

def front(array):
    result = array[0]
    if empty(array):
        result = -1
    return result

def back(array):
    result = array[-1]
    if empty(array):
        result = -1
    return result

