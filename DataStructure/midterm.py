class ArrayList:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None
    
    def insert(self, pos, e):
        if 0 <= pos <= self.size and not self.isFull():
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else: pass
    
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else: pass
    
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isFull(self): return False
    def isEmpty(self): return self.head == None

    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
def factorial(n:int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial(6))
