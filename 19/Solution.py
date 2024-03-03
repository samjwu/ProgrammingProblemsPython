# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = head
        
        for i in range(n):
            lead = lead.next
            
        if lead is None:
            return head.next
            
        pre = head
        
        while lead and lead.next:
            pre = pre.next
            lead = lead.next
            
        pre.next = pre.next.next
        
        return head
