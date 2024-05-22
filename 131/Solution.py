class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                else:
                    start += 1
                    end -= 1
                    
            return True
        
        def backtrack(ans: List[List[str]], s: str, start: int, substrs: List[str]) -> None:
            if start == len(s):
                ans.append(substrs[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(s, start, end):
                    substrs.append(s[start:end+1])
                    backtrack(ans, s, end+1, substrs)
                    substrs.pop()
        
        ans = []
        substrs = []
        
        backtrack(ans, s, 0, substrs)
        
        return ans
