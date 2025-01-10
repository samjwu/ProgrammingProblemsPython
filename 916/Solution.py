class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def calc_freq(word, freq):
            for c in word:
                freq[ord(c) - ord('a')] += 1

        def is_subset(b, a):
            for i in range(26):
                if b[i] > a[i]:
                    print(i)
                    return False
            return True
            
        freq2 = [0] * 26
        for word in words2:
            word_freq = [0] * 26
            calc_freq(word, word_freq)
            for i in range(26):
                freq2[i] = max(freq2[i], word_freq[i])

        ans = []

        for word in words1:
            freq1 = [0] * 26
            calc_freq(word, freq1)
            if is_subset(freq2, freq1):
                ans.append(word)

        return ans
