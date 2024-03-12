# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        beforeHead = ListNode(0, head)

        ptr1 = beforeHead

        # beginning of subseq (exclusive)
        while ptr1 is not None:
            prefixSum = 0
            
            # end of subseq (inclusive)
            ptr2 = ptr1.next

            while ptr2 is not None:
                prefixSum += ptr2.val
                
                # if subseq sums to 0, remove it
                if prefixSum == 0:
                    ptr1.next = ptr2.next
                    
                ptr2 = ptr2.next

            ptr1 = ptr1.next

        return beforeHead.next
