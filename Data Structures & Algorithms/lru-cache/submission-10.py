'''
use a doubly linked list 

Dummy nodes as the head and tail 
The head is where the most recently used node is
the tail is where the lru ndoe is 
ejection happens at the tail

'''

class Node:
    def __init__(self, key=None, val=None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = {}
        self.head = Node()
        self.tail = Node()

        # Come back and see if this initalization needs to be corrected
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dct:
            ## refresh node 
            node = self.dct[key]
            self.remove(node)
            self.add(node)
            return self.dct[key].val
        return -1
        
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next = node
        node.next.prev = node
        self.dct[node.key] = node

    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.dct[node.key]

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            # update the value of node refresh node
            node = self.dct[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return
        # new node
        node = Node(key, value)
        self.add(node)
        if len(self.dct) > self.capacity:
            # eject lru node 
            to_be_deleted = self.tail.prev
            print(f"ejecting key: {to_be_deleted.key}, node: {to_be_deleted.val}")
            self.remove(to_be_deleted)
            



        
