# removing kth person and setting new 0th index
# is equivalent to shifting circle by -k
# (f(n, k) + k) % n = f(n-1, k)
# f(n, k) + k = f(n-1, k) % n
# f(n, k) = (f(n-1, k) - k) % n
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.recurse(n, k) + 1
    
    def recurse(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        return (self.recurse(n-1, k) + k) % n
