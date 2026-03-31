import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        idle = deque([])
        count = Counter(tasks)
        max_heap = list(count.values())
        heapq.heapify_max(max_heap)
        t = 0
        while idle or max_heap:
            t+=1
            if idle :
                if idle[0][1] == t :
                    ops , cool = idle.popleft()
                    heapq.heappush_max(max_heap,ops)
            if max_heap :
                task = heapq.heappop_max(max_heap)
                if task > 1:
                    idle.append([task-1,t+n+1])
        return t
        
