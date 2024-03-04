class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        n = len(tokens)
        
        ans = 0
        score = 0
        
        up = 0
        down = n - 1
        
        while up <= down:
            if power >= tokens[up]:
                power -= tokens[up]
                score += 1
                up += 1
                ans = max(ans, score)
            elif score >= 1:
                power += tokens[down]
                score -= 1
                down -= 1
            else:
                break
        
        return ans
