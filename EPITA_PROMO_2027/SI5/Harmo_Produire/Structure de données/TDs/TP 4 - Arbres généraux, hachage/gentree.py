class GenTree:
    def __init__(self, key, children=None):
        if children is None:
            children = []

        self.key = key
        self.children = children


_example_tree = GenTree(1, [
    GenTree(2, [
        GenTree(7),
        GenTree(8, [
            GenTree(14),
            GenTree(17),
        ]),
    ]),
    GenTree(3),
    GenTree(4, [
        GenTree(10),
        GenTree(12),
    ]),
    GenTree(5)
])


_huge_tree = GenTree(1, [
    GenTree(2, [
        GenTree(6),
        GenTree(7),
        GenTree(8, [
            GenTree(14),
            GenTree(15),
            GenTree(16),
            GenTree(17),
        ]),
    ]),
    GenTree(3),
    GenTree(4, [
        GenTree(9),
        GenTree(10),
        GenTree(11, [
            GenTree(18),
            GenTree(19),
            GenTree(20),
        ]),
        GenTree(12),
    ]),
    GenTree(5, [
        GenTree(13, [
            GenTree(21),
            GenTree(22),
        ])
    ])
])


def size(b):
    # return 1 + sum(size(child) for child in b.children)
    sz = 1
    for child in b.children:
        sz += size(child)
    return sz


def height(b, h=0):
    max_height = h
    for child in b.children:
        max_height = max(max_height, height(child, h + 1))
    return max_height


def epl(b, h=0):
    # if it's a leaf
    if not b.children:
        return h, 1

    sum_epl, leaf_count = 0, 0

    for child in b.children:
        child_epl, child_leaf_count = epl(child, h + 1)
        sum_epl += child_epl
        leaf_count +=  child_leaf_count

    return sum_epl, leaf_count


def ead(b):
    pl, nb_leaves = epl(b)
    return pl / nb_leaves


def prefix(b):
    print(b.key)
    for child in b.children:
        prefix(child)


def suffix(b):
    for child in b.children:
        suffix(child)
    print(b.key)


def search(b, x):
    if b.key == x:
        return b

    if not b.children:
        return None

    for child in b.children:
        s = search(child, x)
        if s is not None:
            return s

    return None

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


def bfs(b):
    q = enqueue(None, b)
    while q is not None:
        q, b = dequeue(q)
        print(b.key)
        for child in b.children:
            q = enqueue(q, child)
