class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)

        if m % 2 == 0:
            half = m // 2 - 1
        else:
            half = m // 2

        front = int(n[0:half+1])

        candidates = []

        # try front and front reversed
        candidates.append(self.generatePalindrome(front, m % 2 == 0))

        # add 1 to front and try
        candidates.append(self.generatePalindrome(front + 1, m % 2 == 0))

        # remove 1 from front and try
        candidates.append(self.generatePalindrome(front - 1, m % 2 == 0))

        # try all 9s closest to n
        candidates.append(10 ** (m - 1) - 1)

        # try power of 10 closest to n, plus 1
        candidates.append(10**m + 1)

        diff = float("inf")

        ans = 0

        num = int(n)

        for candidate in candidates:
            # answer cannot include itself
            if candidate == num:
                continue

            if abs(num - candidate) < diff:
                diff = abs(num - candidate)
                ans = candidate
            elif abs(num - candidate) == diff:
                # return smaller in tie
                ans = min(ans, candidate)

        return str(ans)

    def generatePalindrome(self, front: int, isPalindromeLenEven: bool) -> int:
        """
        Generate remaining back half of palindrome given front half
        """
        ans = front

        # skip middle for odd length palindrome
        if isPalindromeLenEven == False:
            front = front // 10

        while front > 0:
            ans = ans * 10 + front % 10
            front //= 10

        return ans
