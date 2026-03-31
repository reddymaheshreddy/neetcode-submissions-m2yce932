class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        '''
         1

      2     3
      
      4     5
         
         6

     postorder : left right root
     6  4 5 2 3 1

     Alien language uses same letters but order is not same 
     based on the rules of new language the words are sorted
     a < b
     [abc,abc]

     t1: la>lb and b is a suffix of a return ""
     t2: la<lb and a is a suffix of b nothing just pass
     a--b---c---a 
      

     a -> (b,c)
     b -> 

        '''
        order = {}
        for word in words:
            for ch in word:
                if ch not in order:
                    order[ch]=[]
        
        for i in range(len(words)):
            parent =  words[i]
            for j in range(i+1,len(words)):
                child = words[j]
                lp = len(parent)
                lc = len(child)
                prefix  = min(lp,lc)
                if parent[:prefix] == child[:prefix] and lp>lc:
                    return ""
                if parent[:prefix] == child[:prefix] and lp<lc:
                    continue
                p ,c = 0,0
                while p < lp and c < lc:
                    if parent[p] != child[c]:
                        if child[c] not in order[parent[p]]:
                            order[parent[p]].append(child[c])
                        break
                    p+=1
                    c+=1
        visited = set()
        path = set()
        topOrder=[]
        def dfs(letter):
            visited.add(letter)
            path.add(letter)
            for adj in order[letter]:
                if adj in path:
                    return False
                if adj in visited:
                    continue
                if not dfs(adj):
                    return False
            path.remove(letter)
            topOrder.append(letter)
            return True

        for letter in order.keys():
            if letter not in visited:
                if not dfs(letter):
                    return ""
        return "".join(topOrder[::-1])
                
                
                


        
        