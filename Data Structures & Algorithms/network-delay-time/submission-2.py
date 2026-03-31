import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}

        minheap = [(0,k)]
        for src,dst,cost in times:
            adj[src].append((cost,dst))
        visit = set()
        i = 0
        cost = 0
        while minheap and i != n:
            time,node = heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            i+=1
            print(node)
            cost = max(cost,time )
            for cst,dst in adj[node]:
                if dst not in visit:
                    heapq.heappush(minheap,(time+cst,dst))
        if i == n:
            return cost
        else:
            return -1


        