# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        head
        12 --> 3 ---> 4 ---> 6
        """
        


        def inserting(node):
            if not node.next:
                return node.val
            value = inserting(node.next)
            hcf = math.gcd(value,node.val)
            temp = node.next
            node.next = ListNode(hcf)
            node.next.next = temp
            return node.val
        inserting(head)
        return head

        