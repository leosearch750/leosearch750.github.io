class HashTable():
    def __init__(self, capacity, hash_function):
        self.capacity = capacity
        self.hash_function = hash_function
        self.table = [None] * capacity


"""
Linked List implementation used for collision resolution
"""

class LinkedList:
    def __init__(self, val):
        self.elem = val
        self.next = None


def list_prepend(L, val):
    new_head = LinkedList(val)
    new_head.next = L
    return new_head


def list_delete(L, val):
    cursor = L

    if cursor != None and cursor.elem == val:
        L = cursor.next
        return L, True

    while cursor != None:
        if cursor.elem == val:
            prev.next = cursor.next
            cursor = None
            return L, True
        prev = cursor
        cursor = cursor.next

    return L, False


def djb2(s):
    """
    Simple string hashing function taken from http://www.cse.yorku.ca/~oz/hash.html
    """
    res = 5381
    for c in s:
        res = res * 33 + ord(c)
    return res & 0xFFFFFFFF


def insert(t, x):
    h = t.hash_function(x)
    idx = h % t.capacity

    # easy case, no collision
    if t.table[idx] is None:
        t.table[idx] = LinkedList(x)
    # collision handling
    else:
        head = t.table[idx]
        t.table[idx] = list_prepend(head, x)


def find(t, x):
    h = t.hash_function(x)
    idx = h % t.capacity

    head = t.table[idx]
    while head != None:
        if head.elem == x:
            return True
        head = head.next

    return False


def delete(t, x):
    h = t.hash_function(x)
    idx = h % t.capacity

    head = t.table[idx]
    t.table[idx], deleted = list_delete(head, x)
    return deleted


def resize(t, new_capacity):
    new_table = HashTable(new_capacity, t.hash_function)
    for head in t.table:
        while head != None:
            insert(new_table, head.elem)
            head = head.next
    return new_table


"""
Printing utilities
"""

def print_list(L):
    if L is not None:
        cursor = L
        print(L.elem, end="")
        cursor = cursor.next
        while cursor != None:
            print(f" -> {cursor.elem}", end="")
            cursor = cursor.next
    print()


def print_hash_table(t):
    for i in range(t.capacity):
        print(f'[{i:02d}] ', end='')
        print_list(t.table[i])
