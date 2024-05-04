class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        n = len(people)
        
        i = 0
        j = n-1
        
        ans = 0
        
        while i <= j:
            ans += 1
            curr = people[j]
            j -= 1
            
            if i <= j and curr + people[j] <= limit:
                curr += people[j]
                j -= 1
                continue
                
            if i <= j and curr + people[i] <= limit:
                curr += people[i]
                i += 1
            
        return ans
