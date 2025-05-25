class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = defaultdict(int)
        # example: aa or bb 
        extra_doubles = 0
        ans = 0

        for word in words:
            if word[0] == word[1]:
                if freq[word] > 0:
                    # ex: aaaa
                    extra_doubles -= 1
                    freq[word] -= 1
                    ans += 4
                else: 
                    # ex: aa
                    freq[word] += 1
                    extra_doubles += 1
            else:
                if freq[word[::-1]] > 0:
                    # ex: ab...ba
                    ans += 4
                    freq[word[::-1]] -= 1
                else:
                    # ex: ab
                    freq[word] += 1

        if extra_doubles > 0:
            # ex: ...aa...
            ans += 2
        return ans
            