import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        points[i]=[xi,yi]
        


        [0,0]   [2,2]   [3,3]    [2,4]

        '''
        n = len(points)
        adjList ={i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                manDist=abs(x2-x1)+abs(y2-y1)
                adjList[i].append((j,manDist))
                adjList[j].append((i,manDist))
        print(adjList)
        minheap=[(0,0,0)]
        visited = set()
        res = 0 
        while minheap and len(visited) != n:
            print(minheap)
            d,v1,v2 = heapq.heappop(minheap)
            if v1  in visited and v2 in visited :
                continue
            res += d
            print(res)
            if v1 not in visited:
                visited.add(v1)
                for to,cost in adjList[v1]:
                    if to not in visited:
                        
                        heapq.heappush(minheap,(cost,v1,to))
            if v1 != v2 and v2 not in visited:
                visited.add(v2)
                for to,cost in adjList[v2]:
                    if to not in visited:
                        
                        heapq.heappush(minheap,(cost,v2,to))
        return res





        