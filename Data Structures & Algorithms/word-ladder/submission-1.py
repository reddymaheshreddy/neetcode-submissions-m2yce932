class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        def checkwords(w1,w2):
            return sum(a != b for a, b in zip(w1, w2)) == 1
        wordList.append(beginWord)
        adj = {}
        for w1 in wordList:
            if w1 in adj:
                continue
            adj[w1]=[]
            for w2 in wordList:
                if checkwords(w1,w2):
                    adj[w1].append(w2)
        
        visited = set()
        def dfs(word):
            if word == endWord:
                return 1
            visited.add(word)
            count = float("inf")
            for transfer in adj[word]:
                if transfer not in visited:
                    count = min (count,1+dfs(transfer))
            visited.remove(word)
            return count
        count  = dfs(beginWord)
        if count == float("inf"):
            return 0
        else:
            return count 

