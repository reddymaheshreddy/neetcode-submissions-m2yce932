from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1  :  # Quick check: tree must have exactly n-1 edges
            return False
        if n == 1:
            return True
        
        adj={}
        for n1,n2 in edges:
            if n1 in adj:
                adj[n1].append(n2)
            else:
                adj[n1]=[n2]  
            if n2 in adj:
                adj[n2].append(n1)
            else:
                adj[n2]=[n1]
        queue=deque()
        visited=set()
        queue.append((0,-1))
        while queue:
            l=len(queue)
            for _ in range(l):
                node,parent=queue.popleft()
                print(node)
                visited.add(node)
                for nd in adj[node]:
                    if nd in visited and nd!=parent:
                        return False
                    if nd not in visited:
                        queue.append((nd,node))
        for i in range(n):
            if i not in visited:
                return False
        return True

                    
                  
        