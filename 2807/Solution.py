# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            
            return a
        
        ptr = head
        
        while ptr and ptr.next:
            hi = max(ptr.val, ptr.next.val)
            lo = min(ptr.val, ptr.next.val)
            div = gcd(hi, lo)
            
            mid = ListNode(div, ptr.next)
            
            ptr.next = mid
            ptr = ptr.next
            ptr = ptr.next
        
        return head