# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Handle case when lists is empty
            return None
        if len(lists) == 1:  # Base case: if there's only one list, return it
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])   # Recursively divide and merge left half
        right = self.mergeKLists(lists[mid:])  # Recursively divide and merge right half
        
        return self.mergeSortedLinkedLists(left, right)

    def mergeSortedLinkedLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        tail = dummy  # Tail points to the last node in the merged list
        
        # Merge the two lists
        while left and right:
            if left.val <= right.val:
                tail.next = left  # Link the smaller node to the merged list
                left = left.next  # Move the iterator of the left list forward
            else:
                tail.next = right  # Link the smaller node to the merged list
                right = right.next  # Move the iterator of the right list forward
            tail = tail.next  # Move the tail to the newly added node
        
        # Attach the remaining nodes, if any
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next  # Return the head of the merged list
