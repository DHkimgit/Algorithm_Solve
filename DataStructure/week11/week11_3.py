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

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = BSTNode(key, value)
        if self.root is None:
            self.root = new_node
        else:
            insert_bst(self.root, new_node)

    def delete(self):
        if self.root is None:
            return None
        max_node = search_max_bst(self.root)
        if max_node is not None:
            self.root = delete_bst(self.root, max_node.key)
            return max_node
        return None

    def peek(self):
        max_node = search_max_bst(self.root)
        if max_node is not None:
            return max_node
        return None

    def is_empty(self):
        return self.root is None


pq = PriorityQueue()

pq.insert(28, "이팔")
pq.insert(35, "삼오")
pq.insert(19, "일구")
pq.insert(26, "이육")
pq.insert(8, "팔")
pq.insert(45, "사오")
pq.insert(7, "칠")
pq.insert(13, "일삼")
pq.insert(32, "삼이")

for i in range(5):
    print("최대 키 노드 삭제 결과 :", pq.delete().key)

print("최대 키 노드 :", pq.peek().key)