class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects=[ [profit,cap] for profit,cap in zip(profits,capital)]
        projects.sort(key = lambda project:project[1])
        maxheap=[]
        l = len(capital)
        i=0
        curr = 0
        
        while  curr<k:
            while i < l and projects[i][1] <= w:
                heapq.heappush_max(maxheap,projects[i][0])
                i+=1
            if not maxheap :
                break
   
            val = heapq.heappop_max(maxheap)
      
            w+=val
            curr+=1
        return w