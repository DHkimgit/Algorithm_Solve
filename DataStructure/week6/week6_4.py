import copy

class Node:
    def __init__ (self, data, next=None):
        self.data = data 
        self.link = next

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): 
        return self.head == None
    
    def isFull(self): 
        return False

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getRearNode(self):
        node = self.head
        while node.link != None:
            node = node.link
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: 
            return None
        else: 
            return node.data

    def insert(self, pos, data):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link
    
    def append(self, data):
        if not self.isEmpty():
            rear = self.getRearNode()
            rear.link = Node(data, None)
        else:
            self.head = Node(data, None)
    
    def changeData(self, pos, data):
        node = self.getNode(pos)
        node.data = data
    
    def addData(self, pos, data):
        node = self.getNode(pos)
        node.data += data
    
    def subtractData(self, pos, data):
        node = self.getNode(pos)
        node.data -= data
    
    def multipleData(self, pos, data):
        node = self.getNode(pos)
        node.data *= data

    def size(self):
        node = self.head;
        count = 0;
        while node is not None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)
    
class Polynomial:
    def __init__(self, coef):
        self.coef = coef

    def __add__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = LinkedList()

        if(index_self == index_rhs):
            for i in range(index_self):
                result_coef.append(self.coef.getEntry(i) + rhs.coef.getEntry(i))

        elif index_self > index_rhs:
            result_coef = copy.deepcopy(self.coef)
            for i in range(index_rhs):
                # result_coef[i] += rhs.coef.getEntry(i)
                result_coef.addData(i, rhs.coef.getEntry(i))

        else:
            result_coef = copy.deepcopy(rhs.coef)
            for i in range(index_self):
                #result_coef[i] += self.coef[i]
                result_coef.addData(i, self.coef.getEntry(i))
        
        return Polynomial(result_coef)
    
    def __sub__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = LinkedList()

        if(index_self == index_rhs):
            for i in range(index_self):
                # result_coef.append(self.coef[i] - rhs.coef[i])
                result_coef.append(self.coef.getEntry(i) - rhs.coef.getEntry(i))
        
        elif index_self > index_rhs:
            # result_coef = self.coef[:]
            result_coef = copy.deepcopy(self.coef)
            for i in range(index_rhs):
                # result_coef[i] -= rhs.coef[i]
                result_coef.subtractData(i, rhs.coef.getEntry(i))

        else:
            # result_coef = [-coef for coef in rhs.coef[:]]
            node = rhs.coef.head
            while node is not None:
                result_coef.append(-node.data)
                node = node.link
            for i in range(index_self):
                #result_coef[i] += self.coef[i]
                result_coef.addData(i, self.coef.getEntry(i))
        
        return Polynomial(result_coef)
    
    def __mul__(self, rhs):
        index_self = self.degree() + 1
        index_rhs = rhs.degree() + 1
        result_coef = LinkedList()

        if(index_self == index_rhs):
            for i in range(index_self):
                result_coef.append(self.coef.getEntry(i) * rhs.coef.getEntry(i))
        
        elif index_self > index_rhs:
            result_coef = copy.deepcopy(self.coef)
            for i in range(index_rhs):
                #result_coef[i] *= rhs.coef.getEntry(i)
                result_coef.multipleData(i, rhs.coef.getEntry(i))

        else:
            result_coef = copy.deepcopy(rhs.coef)
            for i in range(index_self):
                # result_coef[i] *= self.coef.getEntry(i)
                result_coef.multipleData(i, self.coef.getEntry(i))
        
        return Polynomial(result_coef)
    
    def degree(self):
        return self.coef.size() - 1
    
    def evaluate(self, scalar):
        result = 0
        for i in range(self.degree() + 1):
            result += self.coef.getEntry(i) * (scalar ** i)
        return result
    
    def display(self, message = ""):
        result = []
        first_flag = True
        
        for i in range(self.degree(), -1, -1):
            coef = float(self.coef.getEntry(i))

            if first_flag:
                result.append(f"{coef} x^{i}")
                first_flag = False
            
            else:
                if coef < 0:
                    if i == 0:
                        result.append(f" - {-coef}")
                    else:
                        result.append(f" - {-coef} x^{i}")
                elif coef > 0:
                    if i == 0:
                        result.append(f" + {coef}")
                    else:
                        result.append(f" + {coef} x^{i}")
                else:
                    pass

        print(message + ''.join(result))

    @staticmethod
    def read():
        coef_list = list(map(int, input("최고차항부터 차수를 순서대로 입력하세요: ").split()))
        coef = LinkedList()
        reverse = coef_list[::-1]
        for data in reverse:
            coef.append(data)
        return Polynomial(coef)

a = Polynomial.read()
b = Polynomial.read()
c = a + b
d = a - b
d2 = b - a
e = a * b

a.display("A(x) = ")
b.display("B(x) = ")
c.display("A(x) + B(x) = ")
d.display("A(x) - B(x) = ")
d2.display("B(x) - A(x) = ")
e.display("A(x) * B(x) = ")
print("A(2) + B(2) = ", c.evaluate(2))
