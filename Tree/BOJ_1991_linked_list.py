import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nodes = {}

def get_or_create_node(data):
    if data == '.':
        return None
    if data not in nodes:
        nodes[data] = Node(data)
    return nodes[data]

def perorder(node: Node):
    if node is None:
        return
    print(node.data, end='')
    perorder(node.left)
    perorder(node.right)

def inorder(node: Node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end='')
    inorder(node.right)

def postorder(node: Node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='')

N = int(input())
for _ in range(N):
    data, left, right = input().split()
    parent = get_or_create_node(data)
    parent.left = get_or_create_node(left)
    parent.right = get_or_create_node(right)

root = nodes['A']

perorder(root)
print('')
inorder(root)
print('')
postorder(root)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nodes = {}

def get_or_create_node(data):
    if data == '.':
        return None
    if data not in nodes:
        nodes[data] = Node(data)
    return nodes[data]

