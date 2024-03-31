class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        
        # index of value closest to right bound
        # that is outside the range [minK, maxK]
        outIndex = -1
        
        # index of minK closest to right bound
        closestMinKIndex = -1
        
        # index of maxK closest to right bound
        closestMaxKIndex = -1
        
        for rightBound, number in enumerate(nums):
            if number < minK or number > maxK:
                outIndex = rightBound
                
            if number == minK:
                closestMinKIndex = rightBound
                
            if number == maxK:
                closestMaxKIndex = rightBound
            
            # if outIndex is closer to rightBound than minK/maxK
                # there are 0 subanswers
            # else minK/maxK are closer to rightBound than outIndex
                # so take the smaller index to include both values
                # then (smaller index - outIndex) == number of subarrays
                # or subanswers from outIndex to rightBound
            smallerIndex = min(closestMinKIndex, closestMaxKIndex)
            answer += max(0, smallerIndex - outIndex)
            
        return answer
