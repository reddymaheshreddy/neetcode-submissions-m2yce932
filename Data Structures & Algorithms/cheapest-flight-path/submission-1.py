from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        0 to n-1 airports 
        every airport is connected by a flight
        from,to,price
        one - way flight
        between two airports max can be two flights
        upto n2 flights

        src, dst , k
        k is the maximum number of stops 
        [0,200,100,500]
        k=2 
        loop= k+1
        queue
        [0,0]
        [1,200][2,100][3,500]
        [1,200]

        
    
        '''

        cheapest=[float("inf") for i in range(n)]
        adj={i:[] for i in range(n)}
        for fro,to,price in flights:
            adj[fro].append([to,price])
        cheapest[src]=0
        queue=deque([[src,0]])
        for _ in range(k+1):
            for _ in range(len(queue)):
                node,cost=queue.popleft()
                for to,price in adj[node]:
                    total = price+cost
                    if cheapest[to] > total:
                        cheapest[to] = total
                        queue.append([to,total])
        return cheapest[dst] if cheapest[dst] != float("inf") else -1
        