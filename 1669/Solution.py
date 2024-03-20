# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ansValues = []
        
        index = 0

        ptr1 = list1

        while index < a:
            ansValues.append(ptr1.val)
            ptr1 = ptr1.next
            index += 1

        ptr2 = list2

        while ptr2 is not None:
            ansValues.append(ptr2.val)
            ptr2 = ptr2.next

        while index < b + 1:
            ptr1 = ptr1.next
            index += 1

        while ptr1 is not None:
            ansValues.append(ptr1.val)
            ptr1 = ptr1.next

        ans = None

        for i in range(len(ansValues)):
            node = ListNode(ansValues.pop(), ans)
            ans = node

        return ans
