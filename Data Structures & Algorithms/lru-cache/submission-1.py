"""
Build a LRU cache
if number of keys == capacity
to insert a new key need to delete least used key 
intializing LRUCache looks like this
head ---->node---> tail
     <----    <----
i) Build node class with attributes key , value, prev, next
ii) utility functions in LRUCache delete the first node , delete a node using key , add a node at the end

"""
class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head   # ✅ FIXED

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None   # ✅ cleanup
        node.next = None

    def delete_first(self):
        if self.head.next == self.tail:   # ✅ safety check
            return None
        node = self.head.next
        self.delete(node)
        return node.key

    def add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.delete(node)   # ✅ move to most recent
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.delete(node)
        elif len(self.lookup) == self.capacity:   # ✅ no need for self.current
            del_key = self.delete_first()
            if del_key is not None:
                del self.lookup[del_key]

        node = Node(key, value)
        self.add(node)
        self.lookup[key] = node

        
