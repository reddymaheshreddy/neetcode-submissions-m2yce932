# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [1   ,    2,   3,   4,   5,   6]
        # [(s,f)]
        #        [s]    [f]
        #                 [s]       [f]
        # [0,1,2,3,4,5,6]
        #  [0,6,1,5,2,4,3]
        if not head.next:
            return 
        dummy = head
        slow=head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        print(slow.val)
        def reverse(node):
            nonlocal dummy
            if not node:
                return 
            reverse(node.next)
            temp = dummy.next
            dummy.next = node
            node.next = temp
            dummy = dummy.next.next
        reverse(slow)
        dummy.next = None
        

