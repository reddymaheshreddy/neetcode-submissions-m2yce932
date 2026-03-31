# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        res=[]
        while queue:
            temp=[]
            temp2=[]
            while queue:
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    temp2.append(node.left)
                if node.right:
                    temp2.append(node.right)
            res.append(temp)
            queue.extend(temp2)
        return res