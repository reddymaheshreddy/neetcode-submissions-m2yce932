class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res =[]
        visited = set()
        path = set()
        adj ={}
        for c1,c2 in prerequisites:
            if c2 in adj:
                adj[c2].append(c1)
            else:
                adj[c2]=[c1]
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            if course not in adj:
                res.append(course)
                return True
            path.add(course)
            visited.add(course)
            for c in adj[course]:
                if not dfs(c):
                    return False
            res.append(course)
            path.remove(course)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        res.reverse()
        return res
        
        