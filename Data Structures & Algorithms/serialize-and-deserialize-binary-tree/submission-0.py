# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=""
        def dfs(root):
            nonlocal res
            if not root:
                res+= "null:"
                return
            res+=str(root.val)+':'
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        print(res[:-1])
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        preorder = data.split(":")
        self.i = 0   # global pointer

        def dfs():
            if preorder[self.i] == "null":
                self.i += 1
                return None

            node = TreeNode(int(preorder[self.i]))
            self.i += 1
            print(node.val,self.i)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
