class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        people[i]=weight
        infinte number of boats
        maximum weight limit 
        max two people for each boat
        minimum number of boats

        [5,1,4,2] limit = 6 
        [1,2,3,4,5] limit = 7
        []

        '''
        # sort weights in ascending order
        people.sort()
        left = 0
        right = len(people)-1
        boats = 0
        while left<right:
            if people[left]+people[right] <= limit:
                left +=1
                right -=1
            else:
                right -=1
            boats+=1
        if left == right:
            boats+=1
        return boats

        