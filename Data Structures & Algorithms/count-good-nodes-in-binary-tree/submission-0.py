# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(root,max_val):
            nonlocal total
            if not root:
                return 
            if root.val >= max_val:
                total+=1
                dfs(root.left,root.val)
                dfs(root.right,root.val)
            else:
                dfs(root.left,max_val)
                dfs(root.right,max_val)
        dfs(root,root.val)
        return total


        