class UnionFind:
    def __init__(self,n):
        self.parents ={}
        self.ranks ={}
        for i in range(1,n+1):
            self.parents[i]=i
            self.ranks[i] = 0
    def find(self,n):
        child = n
        parent = self.parents[child]
        while parent != child:
            child = parent
            parent = self.parents[child]
        return parent
    def hasCycle(self,a,b):
        pA,pB = self.find(a),self.find(b)
        if pA == pB:
            return False
        if self.ranks[pA] >self.ranks[pB]:
            self.parents[pB]=pA
        elif self.ranks[pA] < self.ranks[pB]:
            self.parents[pA]=pB
        else:
            self.parents[pB]=pA
            self.ranks[pA]+=1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = UnionFind(len(edges))
        res = [-1,-1]
        for a,b in edges:
            if not dsu.hasCycle(a,b):
                res = [a,b]
        return res

        