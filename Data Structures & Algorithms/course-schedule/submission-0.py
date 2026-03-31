class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()
        adj ={}
        for c1,c2 in prerequisites:
            if c2 in adj:
                adj[c2].append(c1)
            else:
                adj[c2]=[c1]
        def dfs(c):
            if c in path:
                return False
            if c not in adj:
                return True
            visited.add(c)
            path.add(c)
            for course in adj[c]:
                if not dfs(course):
                    return False
            path.remove(c)
            return True
        for i in range(numCourses):
            if i not in visited and i in adj:
                if not dfs(i):
                    return False
        return True


            
