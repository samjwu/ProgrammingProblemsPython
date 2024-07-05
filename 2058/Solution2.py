# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lo = float("inf")
        hi = -1
        
        prev = head
        curr = head.next
        
        currIdx = 1
        
        prevCrit = 0
        firstCrit = 0
        
        while curr.next:
            if (
                (prev.val > curr.val and curr.next.val > curr.val) or
                (prev.val < curr.val and curr.next.val < curr.val)
            ):
                if firstCrit == 0:
                    firstCrit = currIdx
                    prevCrit = currIdx
                else:
                    lo = min(lo, currIdx - prevCrit)
                    prevCrit = currIdx
            
            currIdx += 1
            prev = curr
            curr = curr.next
            
        if lo != float("inf"):
            hi = prevCrit - firstCrit
        else:
            lo = -1
            
        return [lo, hi]
