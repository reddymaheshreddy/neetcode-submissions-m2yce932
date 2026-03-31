import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)
        l = len(max_heap)
        while l > 1:
            stone1 = heapq.heappop_max(max_heap)
            stone2 = heapq.heappop_max(max_heap)
            l-=2
            if stone1 != stone2:
                heapq.heappush_max(max_heap,abs(stone1-stone2))
                l+=1
        if l==0:
            return 0
        else:
            return max_heap[0]


        