class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        
        # lexical order is from 1 to 9
        for start in range(1, 10):
            self.lexical(start, n, ans)

        return ans

    def lexical(self, curr: int, limit: int, ans: List[int]) -> None:
        if curr > limit:
            return
        
        ans.append(curr)

        # continuously keep trying appending 1 to 9
        for digit in range(10):
            num = curr * 10 + digit
            
            if num <= limit:
                # recurse since 111 is before 12
                self.lexical(num, limit, ans)
            else:
                break
