import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        intervals
        [left,right]
        queries[j] = values
        output[j] = length of the shortest interval i l <= value <= r
                      4.    2.    2.    2     2     2
        intervals = [1,1] [2,3] [3,8] [4,6] [4,5] [6,8]
        queries  = [2,3,1,7,6,8]
        """
        res = [-1]*len(queries)
        index_queries=[[val,i] for i,val in enumerate(queries)]
        index_queries.sort(key=lambda val:val[0])
        intervals.sort(key=lambda interval:interval[0])
        minHeap =[]
        i = 0
        li = len(intervals)
        for query,index in index_queries:
            while i < li and intervals[i][0] <= query:
                l = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap,[l,intervals[i][1]])
                i+=1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            if minHeap:
                res[index]=minHeap[0][0]
            else:
                res[index]=-1

        return res


        