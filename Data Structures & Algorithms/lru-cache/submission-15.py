class Node:
    def __init__(self, val: int, key: int):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

    def __str__(self):
        return str(self.val)
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.dct = {}
        
    def remove(self, node):
        # remove at position
        node.next.prev = node.prev
        node.prev.next = node.next


    def insert(self, node):
        
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1

        node = self.dct[key]
        self.remove(node)
        self.insert(node)
        return self.dct[key].val
        
    def put(self, key: int, value: int) -> None:
        node = None
        if key not in self.dct:
            node = Node(value, key)
            self.insert(node)
            self.dct[key] = node
        else:
            node = self.dct[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        if len(self.dct) > self.capacity:
            del self.dct[self.tail.prev.key]
            self.remove(self.tail.prev)
        