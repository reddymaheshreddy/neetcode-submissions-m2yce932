import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_len = 0
        self.min_len = 0

    def addNum(self, num: int) -> None:
        if not self.max_heap or self.max_heap[0] >= num:
            heapq.heappush_max(self.max_heap,num)
            self.max_len+=1
        else:
            heapq.heappush(self.min_heap,num)
            self.min_len+=1
        if abs(self.max_len - self.min_len) > 1:
            if self.max_len > self.min_len:
                val = heapq.heappop_max(self.max_heap)
                self.max_len -=1
                heapq.heappush(self.min_heap,val)
                self.min_len +=1
            else:
                val = heapq.heappop(self.min_heap)
                self.min_len -=1
                heapq.heappush_max(self.max_heap,val)
                self.max_len +=1    

    def findMedian(self) -> float:
        if self.max_len == self.min_len:
            return (self.max_heap[0]+self.min_heap[0])/2
        else:
            if self.max_len > self.min_len:
                return self.max_heap[0]
            else:
                return self.min_heap[0]
        
        