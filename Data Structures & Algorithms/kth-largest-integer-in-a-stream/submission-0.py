import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k = k

        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        l = len(self.min_heap)
        while l > self.k:
            heapq.heappop(self.min_heap)
            l-=1
        return self.min_heap[0]

        
