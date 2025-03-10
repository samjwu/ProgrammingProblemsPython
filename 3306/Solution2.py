class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.count_at_least_k(word, k) - self.count_at_least_k(word, k + 1)

    def count_at_least_k(self, word: str, k: int) -> int:
        """
        Count number of substrings with at least k consonants
        """
        n = len(word)
        ans = 0
        
        left = 0
        right = 0

        vowel_count = {}
        consonant_count = 0

        while right < n:
            c = word[right]

            if self.is_vowel(c):
                vowel_count[c] = vowel_count.get(c, 0) + 1
            else:
                consonant_count += 1

            # shrink window while valid
            while len(vowel_count) == 5 and consonant_count >= k:
                # all substrings with extra chars from current are valid
                ans += n - right

                c_left = word[left]

                if self.is_vowel(c_left):
                    vowel_count[c_left] -= 1
                    if vowel_count[c_left] == 0:
                        del vowel_count[c_left]
                else:
                    consonant_count -= 1

                left += 1

            right += 1

        return ans

    def is_vowel(self, c: str) -> bool:
        return c in "aeiou"
