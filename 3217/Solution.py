# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numset = set(nums)
        
        fake = ListNode()
        fake.next = head
        
        ptr = fake
        
        while ptr.next:
            if ptr.next.val in numset:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        
        return fake.next
