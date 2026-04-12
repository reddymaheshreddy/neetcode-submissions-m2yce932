# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
"""
class Solution: 
    def merge(self,list1,list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        dummy =ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        return dummy.next
    def divide(self,lists,low,high):
        if low == high:
            return lists[low]
        mid = (low + high)//2
        left = self.divide(lists,low,mid)
        right = self.divide(lists,mid+1,high)
        return self.merge(left,right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists,0,len(lists)-1)

    
        