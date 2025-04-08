class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def auto_adaptive_search(L, x):
    for i in range(len(L)):
        if L[i] != x:
            continue

        new_index = i // 2
        # shift all elements between new_index and original index one step to the right
        for j in range(i, new_index, -1):
            L[j] = L[j-1]
        L[new_index] = x

        return True

    return False


def binary_search(L, x):
    def binary_search_rec(L, x, start, end):
        if start >= end:
            return None

        middle = (start + end) // 2

        if L[middle] == x:
            return middle
        elif L[middle] < x:
            return binary_search_rec(L, x, middle + 1, end)
        else: # L[middle] > x
            return binary_search_rec(L, x, start, middle)

    return binary_search_rec(L, x, 0, len(L))


def BST2List(b):
    def recursion(b, L):
        if b == None:
            return
        recursion(b.left, L)
        L.append(b.key)
        recursion(b.right, L)

    L = []
    recursion(b, L)
    return L


def list2BST(L):
    def list2BST_rec(L, start, end):
        if start >= end:
            return None

        middle = (start + end) // 2
        B = BinTree(L[middle], list2BST_rec(L, start, middle), list2BST_rec(L, middle + 1, end))
        return B

    return list2BST_rec(L, 0, len(L))


def isBST(B):
    inf = float('inf')

    def testBST(B, inf, sup):
        if B == None:
            return True

        if sup < B.key or B.key <= inf:
            return False

        return testBST(B.left, inf, B.key) and testBST(B.right, B.key, sup)

    return testBST(B, -inf, inf)


def minBST(b):
    if b.left is None:
        return b.key
    return minBST(b.left)


def maxBST(b):
    if b.right is None:
        return b.key
    return maxBST(b.right)


def search(b, x):
    if b is None:
        return False

    if b.key == x:
        return True

    if x < b.key:
        return search(b.left, x)

    return search(b.right, x)
