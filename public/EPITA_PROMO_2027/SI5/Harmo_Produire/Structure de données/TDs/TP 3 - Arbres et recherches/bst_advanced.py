class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def BST_leaf_insert(b, x):
    if b is None:
        return BinTree(x, None, None)

    if x <= b.key:
        b.left = BST_leaf_insert(b.left, x)
    else:
        b.right = BST_leaf_insert(b.right, x)

    return b


def maxBST(b):
    if b.right is None:
        return b.key
    return maxBST(b.right)


def BST_delete(b, x):
    if b is None:
        return None

    if x == b.key:
        if b.left is not None and b.right is not None:
            b.key = maxBST(b.left)
            b.left = BST_delete(b.left, b.key)
            return b

        if b.left is None:
            return b.right
        else:
            return b.left

    if x < b.key:
        b.left = BST_delete(b.left, x)
    else:
        b.right = BST_delete(b.right, x)
    return b


def BST_cut(b, x):
    if b is None:
        return None, None

    if b.key <= x:
        G = b
        G.right, D = BST_cut(b.right, x)
    else:
        D = b
        G, D.left = BST_cut(b.left, x)

    return G, D


def BST_insert_root(b, x):
    new_root = BinTree(x, None, None)
    new_root.left, new_root.right = BST_cut(b, x)
    return new_root
