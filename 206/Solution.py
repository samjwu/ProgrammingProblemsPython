# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        
        prev = None
        
        while ptr1:
            after = ptr1.next
            
            ptr1.next = prev
            
            prev = ptr1
            
            ptr1 = after
            
        return prev
