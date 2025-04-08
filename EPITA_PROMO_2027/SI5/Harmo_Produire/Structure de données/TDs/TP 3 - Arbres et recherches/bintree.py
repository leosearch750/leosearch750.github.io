class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def size(b):
    if b is None :
        return 0
    else:
        return 1 + size(b.left) + size(b.right)


def height(b):
    if b is None:
        return -1
    else:
        return 1 + max(height(b.left), height(b.right))


def epl(b, h = 0):  # External Path Length
    if b is None:
        return 0, 0

    if b.left is None and b.right is None:
        return h, 1

    epl1, leaf_count1 = epl(b.left, h + 1)
    epl2, leaf_count2 = epl(b.right, h + 1)

    return epl1 + epl2, leaf_count1 + leaf_count2  # returns (EPL, Leaf count)


def ead(b):  # External Average Depth
    if b is None:
        return 0
    (p, n) = epl(b)
    return p / n


def prefix(b):
    if b is not None:
        print(b.key)
        prefix(b.left)
        prefix(b.right)


def infix(b):
    if b is not None:
        infix(b.left)
        print(b.key)
        infix(b.right)


def suffix(b):
    if b is not None:
        suffix(b.left)
        suffix(b.right)
        print(b.key)


def search(x, b):
    if b is None:
        return None

    if x == b.key:
        return b

    res = search(x, b.left)
    if res is None:
        res = search(x, b.right)
    return res


"""
Queue dynamic implementation for BFS
"""

class LinkedList:
    def __init__(self, val):
        self.elem = val
        self.next = None


def enqueue(queue, val):
    node = LinkedList(val)

    if queue == None:
        # circular list
        node.next = node
        return node

    node.next = queue.next
    queue.next = node
    return node


def dequeue(queue):
    if queue == None:
        return None, None

    first = queue.next
    result = first.elem

    # last element
    if queue.next is queue:
        return None, result

    queue.next = first.next
    return queue, result


def is_empty(queue):
    return queue == None


def bfs(b):
    if b is None:
        return

    q = enqueue(None, b)
    while not is_empty(q):
        q, b = dequeue(q)
        print(b.key)
        if b.left is not None:
            q = enqueue(q, b.left)
        if b.right is not None:
            q = enqueue(q, b.right)


def _print_tree(node, padding, arrow, right_sibling):
    if node is None:
        return

    print()
    print(padding, arrow, node.key, sep='', end='')

    padding += '|  ' if right_sibling else '   '
    has_right_child = node.right is not None
    right_arrow = '└──'
    left_arrow = '├──' if has_right_child else right_arrow

    _print_tree(node.left, padding, left_arrow, has_right_child)
    _print_tree(node.right, padding, right_arrow, False)


def print_tree(node):
    if node is None:
        return

    print(node.key, end='')

    has_right_child = node.right is not None
    right_arrow = '└──'
    left_arrow = '├──' if has_right_child else right_arrow

    _print_tree(node.left, '', left_arrow, has_right_child)
    _print_tree(node.right, '', right_arrow, False)

    print()
