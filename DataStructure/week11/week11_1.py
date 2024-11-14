class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

def search_bst(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
       return res
    return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def search_max_bst_recurr(n):
    if n is None or n.right is None:
        return n
    return search_max_bst_recurr(n.right)

def search_min_bst_recurr(n):
    if n is None or n.left is None:
        return n
    return search_min_bst_recurr(n.left)

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
           r.left = n
           return True
        else:
           return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
           r.right = n
           return True
        else:
           return insert_bst(r.right, n)
    else: 
        return False

def insert_bst_iter(r, n):
    current = r
    while True:
        if n.key < current.key:
            if current.left is None:
                current.left = n
                return True
            current = current.left
        elif n.key > current.key:
            if current.right is None:
                current.right = n
                return True
            current = current.right
        else:
            return False

def delete_bst(root, key):
    if root == None: 
        return None
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        
        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst_recurr(self.root)

    def findMin(self):
       return search_min_bst_recurr(self.root)

    def search(self, key):
       return search_bst(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst_iter(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, msg = 'BTSMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

# 28, 35, 19, 26, 8, 45, 7, 13, 32
#             28
#           /   \
#         19     35
#        /  \   / \
#       8   26 32 45
#     / \
#    7   13
data = [28, 35, 19, 26, 8, 45, 7, 13, 32]
value = ["이팔", "삼오", "일구", "이육", "팔", "사오", "칠", "일삼", "삼이"]
map = BSTMap()
map.display("[삽입 전] : ")
for i in range(len(data)) :
    map.insert(data[i],value[i])
    map.display("[삽입 %2d] : "%data[i])

print('[최대 키] : ', map.findMax().key)
print('[최소 키] : ', map.findMin().key)
print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
print('[탐색 27] : ', '성공' if map.search(27) != None else '실패')
print('[탐색 삼이]:', '성공' if map.searchValue("삼이") != None else '실패')
print('[탐색 구]:', '성공' if map.searchValue("구") != None else '실패')
    
map.delete(7)
map.display("[삭제  7] : ")
map.delete(35)
map.display("[삭제 35] : ")
map.delete(19) 
map.display("[삭제 19] : ")
map.delete(28) 
map.display("[삭제 27] : ")