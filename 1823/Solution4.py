# removing kth person and setting new 0th index
# is equivalent to shifting circle by -k
# (f(n, k) + k) % n = f(n-1, k)
# f(n, k) + k = f(n-1, k) % n
# f(n, k) = (f(n-1, k) - k) % n
# iterative solution is recursive solution backwards
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        
        for i in range(2, n+1):
            ans = (ans + k) % i
        
        return ans + 1
