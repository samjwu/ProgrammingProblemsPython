# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        accumulate = None
        
        while ptr is not None:
            if ptr.val == 0:
                if accumulate != None:
                    accumulate.next = ptr.next
                    accumulate = None
            else:
                if accumulate == None:
                    accumulate = ptr
                else:
                    accumulate.val += ptr.val
                    
            ptr = ptr.next
            
        return head.next
