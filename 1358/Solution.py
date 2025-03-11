class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        window = [0] * 3
        left = 0
        right = 0

        while right < n:
            window[ord(s[right]) - ord("a")] += 1

            while self.isValidWindow(window):
                # add current window
                # and all substrings by adding chars to the right
                ans += n - right

                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return ans

    def isValidWindow(self, window: list) -> bool:
        for freq in window:
            if freq <= 0:
                return False

        return True
