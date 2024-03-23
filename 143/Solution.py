# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get middle
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse latter half
        prev = None
        curr = slow.next
        
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
            
        slow.next = None
        
        # merge halves
        ptr1 = head
        ptr2 = prev
        
        while ptr2:
            after = ptr1.next
            ptr1.next = ptr2
            ptr1 = ptr2
            ptr2 = after
