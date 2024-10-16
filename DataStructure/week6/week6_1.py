class Node:
    def __init__ (self, data, link = None):
        self.data = data 
        self.link = link

class LinkedStack :
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, data):
        new = Node(data, self.top)
        self.top = new

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    def size(self):
        node = self.top
        count = 0
        while not node == None :
            node = node.link
            count += 1

    def __str__(self):
        arr = []
        node = self.top
        while not node == None :
            arr.append(node.data)
            node = node.link
        return str(arr)
    
def precedence (op):
    if   (op=='(' or op==')'): return 0;
    elif (op=='+' or op=='-'): return 1;
    elif (op=='*' or op=='/'): return 2;
    else : return -1

def InfixToPostfix(expr):
    s = LinkedStack()
    output = []

    for term in expr :
        if term in '(' :
            s.push('(')

        elif term in ')' :
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' :
                    break;
                else :
                    output.append(op)

        elif term in "+-*/" :
            while not s.isEmpty() :
                op = s.peek()
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else :
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop())

    return output

def evalPostfix( expr ):
    s = LinkedStack()
    for token in expr :
        if token in "+-*/" :
            val2 = s.pop()
            val1 = s.pop()
            if   (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) )

    return s.pop()

exp = list(map(str, input("입력 수식(공백 분자로 분리) = ").split()))
exp_infix = InfixToPostfix(exp)
print("중위 표기 : ", exp)
print("후위 표기 : ", exp_infix)
print("계산 결과 : ", evalPostfix(exp_infix))
