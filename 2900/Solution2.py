class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        memo = [1] * n
        # use this list to track subseq
        prev = [-1] * n
        hi = 1
        idx = 0

        for i in range(1, n):
            # track hi and prev for longest current subseq ending at i
            temp_hi = 1
            temp_prev = -1

            # prepend to subseq moving backwards from i
            for j in range(i-1, -1, -1):
                if groups[i] != groups[j] and memo[j] + 1 > temp_hi:
                    temp_hi = memo[j] + 1
                    temp_prev = j

            memo[i] = temp_hi
            prev[i] = temp_prev

            if memo[i] > hi:
                hi = memo[i] 
                idx = i

        # build subseq in reverse using prev list
        ans = []
        i = idx
        
        while i != -1:
            ans.append(words[i])
            i = prev[i]

        return ans[::-1]
