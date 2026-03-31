class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj ={}
        for n1,n2 in edges:
            if n1 in adj:
                adj[n1].append(n2)
            else:
                adj[n1]=[n2]
            if n2 in adj:
                adj[n2].append(n1)
            else:
                adj[n2]=[n1]
        visited = set()
        count = 0
        def dfs(node):
            if node in visited :
                return 
            visited.add(node)
            if node not in adj:
                return 
            for n1 in adj[node]:
                dfs(n1)
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count