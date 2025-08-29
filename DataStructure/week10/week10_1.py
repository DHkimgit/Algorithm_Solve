class CircularQueue:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            pass
    
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
    
    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
    
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
    def isLeaf(self):
        return self.left is None and self.right is None

# 후위
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 전위
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
# 중위
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
        
# 레벨 
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None: 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None: 
        return 0
    elif n.isLeaf(): 
        return 1
    else: 
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None: 
        return 0
    
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    if hLeft > hRight: 
        return hLeft + 1
    else:
        return hRight + 1

# 8.19 이진트리가 완전 이진트리인지를 검사하는 연산 구현
def is_complete_binary_tree(root):
    queue = CircularQueue()
    queue.enqueue(root)
    flag = False

    while not queue.isEmpty():
        n = queue.dequeue()

        if n.left is not None:
            if flag:
                return False
            queue.enqueue(n.left)
        else:
            flag = True
        
        if n.right is not None:
            if flag:
                return False
            queue.enqueue(n.right)
        else:
            flag = True
            
    return True

# 8.20 임의의 node의 레벨을 구하는 연산
def level(root, node):
    queue = CircularQueue()
    queue.enqueue((root, 1))

    while not queue.isEmpty():
        current, current_level = queue.dequeue()

        if current == node:
            return current_level

        if current.left is not None:
            queue.enqueue((current.left, current_level + 1))

        if current.right is not None:
            queue.enqueue((current.right, current_level + 1))

    return 0

# 8.21 균형잡힌 트리인지 검사하는 함수
def is_balanced(root):
    if root is None:
        return True
        
    left_height = calc_height(root.left)
    right_height = calc_height(root.right)

    if abs(left_height - right_height) >= 2:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)

# 8.22 경로의 길이의 합을 구하는 함수
def path_length(root):
    queue = CircularQueue()
    queue.enqueue((root, 0))
    result = 0

    while not queue.isEmpty():
        current, current_level = queue.dequeue()
        result += current_level

        if current.left is not None:
            queue.enqueue((current.left, current_level + 1))

        if current.right is not None:
            queue.enqueue((current.right, current_level + 1))

    return result


# 8.19 완전 이진트리 검사 테스트 코드

# 완전 이진트리인 경우
#       1
#     /   \
#    2     3
#   / \   /
#  4   5 6
complete_tree_node4 = TNode(4, None, None)
complete_tree_node5 = TNode(5, None, None)
complete_tree_node6 = TNode(6, None, None)
complete_tree_node2 = TNode(2, complete_tree_node4, complete_tree_node5)
complete_tree_node3 = TNode(2, complete_tree_node6, None)
complete_tree_node1 = TNode(1, complete_tree_node2, complete_tree_node3)


# 완전 이진트리가 아닌 경우
#       1
#     /   \
#    2     3
#     \   /
#      5 6
incomplete_tree_node5 = TNode(5, None, None)
incomplete_tree_node6 = TNode(6, None, None)
incomplete_tree_node2 = TNode(2, None, incomplete_tree_node5)
incomplete_tree_node3 = TNode(2, incomplete_tree_node6, None)
incomplete_tree_node1 = TNode(1, incomplete_tree_node2, incomplete_tree_node3)

# 완전 이진트리가 아닌 경우
#       1
#     /   \
#    2     3
#  /      /
# 4      6

incomplete2_tree_node6 = TNode(6, None, None)
incomplete2_tree_node4 = TNode(4, None, None)
incomplete2_tree_node2 = TNode(2, incomplete2_tree_node4, None)
incomplete2_tree_node3 = TNode(2, incomplete2_tree_node6, None)
incomplete2_tree_node1 = TNode(1, incomplete2_tree_node2, incomplete2_tree_node3)

# 완전 이진트리가 아닌 경우
#             1
#           /   \
#          2     3
#        /  \   / \
#       4   5  6   7
#     / \
#    8   9
#  / \
# 10 11
incomplete3_tree_node10 = TNode(10, None, None)
incomplete3_tree_node11 = TNode(11, None, None)
incomplete3_tree_node9 = TNode(9, None, None)
incomplete3_tree_node5 = TNode(5, None, None)
incomplete3_tree_node6 = TNode(6, None, None)
incomplete3_tree_node7 = TNode(7, None, None)
incomplete3_tree_node8 = TNode(8, incomplete3_tree_node10, incomplete3_tree_node11)
incomplete3_tree_node4 = TNode(4, incomplete3_tree_node8, incomplete3_tree_node9)
incomplete3_tree_node2 = TNode(2, incomplete3_tree_node4, incomplete3_tree_node5)
incomplete3_tree_node3 = TNode(3, incomplete3_tree_node6, incomplete3_tree_node7)
incomplete3_tree_node1 = TNode(1, incomplete3_tree_node2, incomplete3_tree_node3)


result_complete = is_complete_binary_tree(complete_tree_node1)
result_incomplete = is_complete_binary_tree(incomplete_tree_node1)
result_incomplete2 = is_complete_binary_tree(incomplete2_tree_node1)
result_incomplete3 = is_complete_binary_tree(incomplete3_tree_node1)
print("완전 이진트리 여부 검사 (완전 이진트리 case1): ", end='')
print(result_complete)
print("완전 이진트리 여부 검사 (완전 이진트리 아닌 경우 case2): ", end='')
print(result_incomplete)
print("완전 이진트리 여부 검사 (완전 이진트리 아닌 경우 case3): ", end='')
print(result_incomplete2)
print("완전 이진트리 여부 검사 (완전 이진트리 아닌 경우 case4): ", end='')
print(result_incomplete3)

# 8.20 트리의 노드 레벨 검사 함수 테스트 코드
#       1
#     /   \
#    2     3
#   / \   /
#  4   5 6
complete_tree_node4_level = level(complete_tree_node1, complete_tree_node4)
complete_tree_node2_level = level(complete_tree_node1, complete_tree_node2)
complete_tree_node1_level = level(complete_tree_node1, complete_tree_node1)
incomplete_tree_node5_level = level(complete_tree_node1, incomplete_tree_node5)

print("트리의 노드 레벨 검사(노드 4) : ", end='')
print(complete_tree_node4_level)
print("트리의 노드 레벨 검사(노드 2) : ", end='')
print(complete_tree_node2_level)
print("트리의 노드 레벨 검사(노드 1) : ", end='')
print(complete_tree_node1_level)
print("트리의 노드 레벨 검사(트리의 노드가 아닌 경우) : ", end='')
print(incomplete_tree_node5_level)

# 8.21 균형잡힌 트리 검사 함수 테스트 코드

# 균형잡힌 트리
#       A
#     /   \
#    B     E
#  /  \     \
# C   D      F

nodeC = TNode("C", None, None)
nodeD = TNode("D", None, None)
nodeF = TNode("F", None, None)
nodeB = TNode("B", nodeC, nodeD)
nodeE = TNode("E", None, nodeF)
nodeA = TNode("E", nodeB, nodeE)
result = is_balanced(nodeA)
if result:
    print("균형잡인 트리입니다")
else:
    print("균형잡인 트리가 아닙니다")

# 불균형 트리
#         A
#       /   \
#      B     E
#    /     
#   C       
#  /
# F

nodef = TNode("F", None, None)
nodec = TNode("C", nodef, None)
nodeb = TNode("B", nodec, None)
nodee = TNode("E", None, None)
nodea = TNode("A", nodeb, nodee)

result = is_balanced(nodea)
if result:
    print("균형잡인 트리입니다")
else:
    print("균형잡인 트리가 아닙니다")

# 8.21 트리의 전체 경로 길이 계산 함수 테스트 코드

# case 1
#       A
#     /   \
#    B     E
#  /  \     \
# C   D      F

# case2
#         A
#       /   \
#      B     E
#    /     
#   C       
#  /
# F
case1_length = path_length(nodeA)
case2_length = path_length(nodea)

print(f"전체 경로의 길이는 {case1_length}입니다.")
print(f"전체 경로의 길이는 {case2_length}입니다.")