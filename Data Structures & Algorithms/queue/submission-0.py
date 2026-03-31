class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        tl=Node(value)
        temp=self.tail.prev
        tl.next=self.tail
        self.tail.prev=tl
        tl.prev=temp
        temp.next=tl

    def appendleft(self, value: int) -> None:
        hd=Node(value)
        temp=self.head.next
        self.head.next=hd
        hd.prev=self.head
        temp.prev=hd
        hd.next=temp

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        temp=self.tail.prev
        data=temp.value
        temp.prev.next=self.tail
        self.tail.prev=temp.prev
        return data


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        temp=self.head.next
        data=temp.value
        self.head.next=temp.next
        temp.next.prev=self.head
        return data
