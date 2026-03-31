"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue=deque([node])
        nodes ={node.val:Node(node.val)}
        while queue:
            n = queue.popleft()
            for adj in n.neighbors:
                if adj.val not in nodes:
                    nodes[adj.val]=Node(adj.val)
                    queue.append(adj)
                nodes[n.val].neighbors.append(nodes[adj.val])
        return nodes[node.val]