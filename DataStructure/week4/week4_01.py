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
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False
    
    return stack.isEmpty()

file_name = str(input("읽고 싶은 .py 파일의 제목(위치)을 입력하세요: "))
lines = readPythonFile(file_name)

for line in lines:
    if line.strip():
        if checkBrackets(line):
            print(line.strip() + " ---> True")
        else:
            print(line.strip() + " ---> False")

def read_file_lines_str(filename):
    with open(filename, 'r') as infile:
        read_str = infile.read()  # 파일의 모든 줄을 읽어 리스트로 반환
    return read_str  # 각 줄의 공백 제거 후 리스트로 반환

# print(lines)
# /home/dukekim001/Algorithm/Algorithm_Solve/DataStructure/week4/Test.py
# /home/dukekim001/Algorithm/Algorithm_Solve/DataStructure/week1/week1_02_01.py
# def checkBrackets(statement):
#     stack = ArrayStack(100)
#     for ch in statement:
        
#         if ch=='{' or ch=='[' or ch=='(' :
#             stack.push(ch)
        
#         elif ch=='}' or ch==']' or ch==')' :
#             if stack.isEmpty() :
#                 return 2
#             else :
#                 left = stack.pop()
#                 if (ch == "}" and left != "{") or \
#                    (ch == "]" and left != "[") or \
#                    (ch == ")" and left != "(") :
#                     return 3
    
#     if stack.isEmpty(): return 0
#     else: return 1 


# 읽어들인 줄 출력
# if lines:
#     print("파일 내용:")
#     for idx, line in enumerate(lines, start=1):
#         print(f"{idx}: {line}")
# else:
#     print("파일을 읽을 수 없습니다.")

# n = int(input("소스코드의 줄 수를 입력하세요"))
# data = [sys.stdin.readline().strip() for i in range(n)]

def checkBracketsWithPosition(lines):
    stack = ArrayStack(1000)
    for line_num, line in enumerate(lines):
        for char_num, ch in enumerate(line):
            if ch in "{[(":
                stack.push((ch, line_num, char_num))
            elif ch in "}])":
                if stack.isEmpty():
                    return (2, line_num, char_num)
                else:
                    left, left_line, left_char = stack.pop()
                    if (ch == "}" and left != "{") or \
                       (ch == "]" and left != "[") or \
                       (ch == ")" and left != "("):
                        return (3, line_num, char_num)

    if not stack.isEmpty():
        
        left, left_line, left_char = stack.pop()
        return (1, left_line, left_char)

    return (0, -1, -1)  # 올바른 괄호

def interpretResultWithPosition(lines, result):
    if result[0] == 0:
        return f"올바른 괄호"
    elif result[0] == 1:
        return f"조건 1 위반: 라인 {result[1] + 1}, 문자 {result[2] + 1}"
    elif result[0] == 2:
        return f"조건 2 위반: 라인 {result[1] + 1}, 문자 {result[2] + 1}"
    elif result[0] == 3:
        return f"조건 3 위반: 라인 {result[1] + 1}, 문자 {result[2] + 1}"
    
# print(f"Test 1: {interpretResultWithPosition(data, checkBracketsWithPosition(data))}")

# s1 = "{ A[ (i+1) ] = 0; } "
# s2 = "if( (i==0) && (j==0)"
# s3 = "A[ ( i+1 ] ) = 0;   "
# s4 = "A](1%2) "

# def interpretResult(statement, result):
#     if result == 0:
#         return f"{statement} ---> True"
#     elif result == 1:
#         return f"{statement} ---> 조건 1 위반"
#     elif result == 2:
#         return f"{statement} ---> 조건 2 위반"
#     elif result == 3:
#         return f"{statement} ---> 조건 3 위반"

# print(interpretResult(s1, checkBrackets(s1)))
# print(interpretResult(s2, checkBrackets(s2)))
# print(interpretResult(s3, checkBrackets(s3)))
# print(interpretResult(s4, checkBrackets(s4)))
