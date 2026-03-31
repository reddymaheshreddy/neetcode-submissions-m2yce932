class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        pre = [a,b]
        b is pre-req of a
        numCourses 

        1 ---> 2 ----->3 ----> 1
        1 --- > 0 
        .
        .
        .> 2
        """
        adj = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[b].append(a)
        topOrder=[]
        path = set()
        visited = set()
        def dfs(course):
            if course in visited :
                return True
            visited.add(course)
            path.add(course)
            for neigh in adj[course]:
                if neigh in path:
                    return False
                if not dfs(neigh):
                    return False
            path.remove(course)
            topOrder.append(course)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        topOrder.reverse()
        return topOrder