# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_order = []
        sub_order = []

        def preorder(root, nums):
            if not root:
                nums.append(None)
                return
            nums.append(root.val)
            preorder(root.left, nums)
            preorder(root.right, nums)

        preorder(root, root_order)
        preorder(subRoot, sub_order)

        root_str = ",".join(map(str, root_order))
        sub_str = ",".join(map(str, sub_order))

        return sub_str in root_str
