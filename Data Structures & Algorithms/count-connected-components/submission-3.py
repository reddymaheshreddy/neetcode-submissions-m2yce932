class UnionFind:
    def __init__(self,n):
        
        self.parents={i:i for i in range(n)}
        self.ranks ={i:0 for i in range(n)}
    def findParent(self,node):
        if node != self.parents[node]:
            self.parents[node] = self.findParent(self.parents[node])
        return self.parents[node]
    def addEdge(self,u,v):
        parent1=self.findParent(u)
        parent2=self.findParent(v)
        if parent1 == parent2:
            return
        if self.ranks[parent1] == self.ranks[parent2]:
            self.ranks[parent1]+=1
            self.parents[parent2]=parent1
        elif self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1]=parent2
        else:
            self.parents[parent2]=parent1
       

    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Going to solve using Union set

        step 1: assign every's parent to itself
        step 2: intialize every node's rank to 0
        step 3:
                a) for given edge find rank for both vertices 
                b) if their ranks are equal increase first vertex's rank by 1 and assign second
                c) if they are not equal 
        


        '''
        disjoint = UnionFind(n)
        for u,v in edges:
            disjoint.addEdge(u,v)
        return len({disjoint.findParent(i) for i in range(n)})

        