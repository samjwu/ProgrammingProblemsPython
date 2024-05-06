# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        curr = head

        while curr:
            stk.append(curr)
            curr = curr.next

        curr = stk.pop()
        hi = curr.val
        ans = ListNode(hi)

        while stk:
            curr = stk.pop()
            
            if curr.val < hi:
                continue
            else:
                node = ListNode(curr.val)
                node.next = ans
                ans = node
                hi = curr.val

        return ans
