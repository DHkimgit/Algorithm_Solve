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

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: 
            return None
        else : return node.data

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
    

L = LinkedList()
    
print("최초   ", L)
L.insert(0, 10)
L.insert(0, 20)
L.insert(1, 30)
L.insert(L.size(), 40)
L.insert(2, 50)
print("삽입x5 ", L)
L.delete(2)
print("삭제(2)", L)
L.delete(L.size()-1)
print("삭제(E)", L)
L.delete(0)
print("삭제(0)", L)
