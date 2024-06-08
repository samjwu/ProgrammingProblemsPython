class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        remainder = 0
        # map remainder to index it was seen at
        seenRemainders = {0: -1}
        
        for i in range(n):
            remainder = (remainder + nums[i]) % k
            
            # found subarray with sum % k == 0
            if remainder in seenRemainders:
                # subarray size >= 2
                if i - seenRemainders[remainder] >= 2:
                    return True
            else:
                seenRemainders[remainder] = i
                
        return False
