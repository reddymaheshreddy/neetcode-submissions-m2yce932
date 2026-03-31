class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        itr = self.head
        while index > 0 and itr:
            itr = itr.next
            index -= 1
        if itr is None:
            return -1  # Return -1 if index is out of bounds
        return itr.data

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        if index == 0 and self.head:
            self.head = self.head.next
            return True
        itr = self.head
        while index > 1 and itr:
            itr = itr.next
            index -= 1
        if itr is None or itr.next is None:
            return False  # Invalid index
        itr.next = itr.next.next
        return True

    def getValues(self):
        itr = self.head
        arr = []
        while itr:
            arr.append(itr.data)
            itr = itr.next
        return arr

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(1)
    ll.insertTail(2)
    ll.insertHead(3)
    print(ll.getValues())
