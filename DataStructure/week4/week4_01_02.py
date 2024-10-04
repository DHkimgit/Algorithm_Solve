import sys
class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity	
        self.top = -1

    def isEmpty(self) :
       return self.top == -1

    def isFull(self) :
       return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else: pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def __str__(self):
        return str(self.array[0:self.top+1][::-1])

    def size(self): 
        return self.top+1
    
def readPythonFile(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    return lines

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        
        if ch=='{' or ch=='[' or ch=='(' :
            stack.push(ch)
        
        elif ch=='}' or ch==']' or ch==')' :
            if stack.isEmpty() :
                return 2
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return 3
    
    if stack.isEmpty(): return 0
    else: return 1 

file_name = str(input("읽고 싶은 .py 파일의 제목(위치)을 입력하세요: "))
lines = readPythonFile(file_name)

for line in lines:
    if line.strip():
        if checkBrackets(line) == 0:
            print(line.strip() + " ---> True")
        elif checkBrackets(line) == 1:
            print(line.strip() + " ---> False, 조건 1 위반")
        elif checkBrackets(line) == 2:
            print(line.strip() + " ---> False, 조건 2 위반")
        else:
            print(line.strip() + " ---> False, 조건 3 위반")
