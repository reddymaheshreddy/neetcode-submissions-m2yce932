from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        n airports 
        0 to n-1
        [from,to,price]
        src 
        dst
        k
        [0,inf,inf,inf,inf]
        '''
        distances = [ float("inf") for _ in range(n)]
        distances[src]=0
        adj = {i:[] for i in range(n)}
        for i,j,price in flights:
            adj[i].append([j,price])
        queue = deque([[src,0]])
        for _ in range(k+1):
            l = len(queue)
            for _ in range(l):
                airport,price = queue.popleft()
                for to,cost in adj[airport]:
                    if cost + price >= distances[to]:
                        continue
                    distances[to] = cost + price
                    queue.append([to,distances[to]])
        return distances[dst] if distances[dst] != float("inf") else -1
        
        