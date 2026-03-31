# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        dummy = ListNode(0)
        res = dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node = ListNode(curr1.val)
                curr1=curr1.next
            else:
                node = ListNode(curr2.val)
                curr2=curr2.next
            res.next=node
            res=res.next
        if curr1:
            res.next = curr1
        if curr2:
            res.next = curr2
        return dummy.next
        