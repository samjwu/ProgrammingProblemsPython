class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # convert to linked list
        # reason: since there is a duplicate, there is a loop
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # floyd cycle detection algorithm to get start of loop
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
