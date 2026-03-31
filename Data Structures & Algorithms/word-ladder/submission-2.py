from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        wordList.append(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            l = len(wordList)
            for i in range(l):
                pattern = word[:i]+"*"+word[i+1:]
                patterns[pattern].append(word)
        adj = defaultdict(list)
        for words in patterns.values():
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        adj[w1].append(w2)
        queue = deque([[beginWord,1]])
        visited = set()
        while queue:
            word,length = queue.popleft()
            visited.add(word)
            for neighbor in adj[word]:
                if neighbor == endWord:
                    return length+1
                if neighbor not in visited:
                    queue.append([neighbor,length+1])
        return 0
