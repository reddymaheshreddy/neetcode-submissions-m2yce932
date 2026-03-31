# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum_length = 0
        def dfs(root):
            nonlocal maximum_length
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maximum_length = max(maximum_length,1+left+right)
            return 1 + max(left,right)
        dfs(root)
        return maximum_length - 1
        