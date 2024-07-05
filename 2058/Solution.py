# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        criticals = []
        
        n = len(nums)
        
        for i in range(1, n-1):
            if self.isCritical(nums, i):
                criticals.append(i)
          
        m = len(criticals)
        
        if m < 2:
            return [-1, -1]
        
        hi = criticals[m-1] - criticals[0]
        lo = float("inf")
        
        for i in range(1, m):
            lo = min(lo, criticals[i] - criticals[i-1])
        
        if lo == float("inf"):
            lo = -1
        
        return [lo, hi]
    
    def isCritical(self, nums: List[int], idx: int) -> bool:
        return (
            (nums[idx-1] > nums[idx] and nums[idx+1] > nums[idx]) or 
            (nums[idx-1] < nums[idx] and nums[idx+1] < nums[idx])
        )
