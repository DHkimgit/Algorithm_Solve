class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

def treeSearch(t: BSTNode, x: int):
    """
    이진 탐색 트리에서 키 x를 검색합니다.

    Args:
        t: 트리의 루트 노드
        x: 검색하고자 하는 키

    Returns:
        키 x를 가진 노드. 키 x가 트리에 없으면 None을 반환합니다.
    """
    if t is None or t.key == x:
        return t
    if x < t.key:
        return treeSearch(t.left, x)
    else:
        return treeSearch(t.right, x)

def treeInsert(t: BSTNode, x: int):
    """
    이진 탐색 트리에 키 x를 삽입합니다.

    Args:
        t: 트리의 루트 노드
        x: 삽입하고자 하는 키

    Returns:
        수정된 트리의 루트 노드
    """
    if t is None:
        r = BSTNode(x)
        return r
    if x < t.key:
        t.left = treeInsert(t.left, x)
        return t
    else:
        t.right = treeInsert(t.right, x)
        return t

def treeDelete(root: BSTNode, r: BSTNode):
    """
    이진 탐색 트리에서 노드 r을 삭제합니다.

    Args:
        root: 트리의 루트 노드
        r: 삭제하고자 하는 노드

    Returns:
        수정된 트리의 루트 노드
    """
    if r is None:
        return root  # 삭제할 노드가 없으면 그냥 반환

    # r이 루트 노드인 경우
    if r == root:
        root = deleteNode(r)
        return root
    else:
        # r의 부모 노드를 찾습니다.
        p = find_parent(root, r)

        if p is None:
            return root # 부모 노드를 찾지 못하면 그냥 반환 (에러 처리)

        if r == p.left:
            p.left = deleteNode(r)
        else:
            p.right = deleteNode(r)
        return root

def find_parent(root, node):
    """
    주어진 노드의 부모 노드를 찾습니다.

    Args:
        root: 트리의 루트 노드
        node: 부모 노드를 찾을 노드

    Returns:
        node의 부모 노드.  node가 루트 노드이거나 부모 노드를 찾지 못하면 None을 반환합니다.
    """
    if root is None or root == node:
        return None

    if root.left == node or root.right == node:
        return root

    if node.key < root.key:
        return find_parent(root.left, node)
    else:
        return find_parent(root.right, node)


def deleteNode(r):
    """
    주어진 노드를 삭제하고, 삭제 후 적절한 노드를 반환합니다.

    Args:
        r: 삭제할 노드

    Returns:
        삭제 후 대체될 노드 (None, r.left, r.right, 또는 r)
    """
    if r.left is None and r.right is None:
        return None
    elif r.left is None and r.right is not None:
        return r.right
    elif r.left is not None and r.right is None:
        return r.left
    else:
        # Successor 찾기
        s = r.right
        parent = r  # s가 r.right인 경우를 대비해 초기화
        while s.left is not None:
            parent = s
            s = s.left

        r.key = s.key

        if s == r.right:
            r.right = s.right
        else:
            parent.left = s.right

        return r
    
if __name__ =="__main__":
    root = None
    root = treeInsert(root, 50)
    root = treeInsert(root, 30)
    root = treeInsert(root, 20)
    root = treeInsert(root, 40)
    root = treeInsert(root, 70)
    root = treeInsert(root, 60)
    root = treeInsert(root, 80)


    