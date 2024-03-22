# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        n = len(vals)
        
        for i in range(n//2):
            if vals[i] != vals[n-1-i]:
                return False
            
        return True
