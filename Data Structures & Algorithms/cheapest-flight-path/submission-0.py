class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = [float("inf") for _ in range(n)]
        res[src] = 0
        for _ in range(k+1):
            temp = res[:]
            for src,to,cost in flights:
                if res[src] == float("inf"):
                    continue
                cst = res[src] + cost
                if cst < temp[to]:
                    temp[to] = cst
            res = temp[:]
        return -1 if res[dst] == float("inf") else res[dst]
        