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

    def __str__(self) :
        return str(self.array[0:self.top+1][::-1])

    def size(self) : return self.top+1

def precedence (op):
    if   (op=='(' or op==')'): return 0;
    elif (op=='+' or op=='-'): return 1;
    elif (op=='*' or op=='/'): return 2;
    else : return -1

def InfixToPostfix(expr):
    s = ArrayStack(100)
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
    s = ArrayStack(100)
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

