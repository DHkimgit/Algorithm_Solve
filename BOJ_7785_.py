import sys

storage = {}

for _ in range(int(sys.stdin.readline())):
    name, commend = sys.stdin.readline().rstrip().split()

    if commend == 'enter':
        storage[name] = 'enter'
    
    else:
        if storage[name]:
            del storage[name]

for people in sorted(storage, reverse=True):
    print(people)
            
