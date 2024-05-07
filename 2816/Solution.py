# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        tail = self.revList(head)
        
        carry = 0
        prev = None
        curr = tail

        while curr is not None:
            curr.val = curr.val * 2 + carry            
            carry = curr.val // 10
            curr.val = curr.val % 10
            
            prev = curr
            curr = curr.next

        if carry > 0:
            prev.next = ListNode(carry)

        ans = self.revList(tail)

        return ans

    def revList(self, node: ListNode) -> ListNode:
        prev = None
        curr = node

        while curr is not None:
            nextNode = curr.next

            curr.next = prev
            
            prev = curr

            curr = nextNode

        return prev
