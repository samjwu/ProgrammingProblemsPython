# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for j in range(n)] for i in range(m)]
        
        i = 0
        j = 0
        
        while head:
            while head and j < n and ans[i][j] == -1:
                ans[i][j] = head.val
                head = head.next
                j += 1
            
            j -= 1
            i += 1
            
            while head and i < m and ans[i][j] == -1:
                ans[i][j] = head.val
                head = head.next
                i += 1
                
            i -= 1
            j -= 1
            
            while head and j >= 0 and ans[i][j] == -1:
                ans[i][j] = head.val
                head = head.next
                j -= 1
                
            j += 1
            i -= 1
            
            while head and i >= 0 and ans[i][j] == -1:
                ans[i][j] = head.val
                head = head.next
                i -= 1
                
            i += 1
            j += 1
                
        return ans
