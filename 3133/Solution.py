class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = 0

        # 1st element is x
        # only need to find n-1 remaining numbers        
        n -= 1

        # binary form of x and n-1
        binaryX = [0] * 64
        binaryN = [0] * 64
        for i in range(64):
            binaryX[i] = (x >> i) & 1
            binaryN[i] = (n >> i) & 1

        # replace 0s in x with bits in n-1
        posX = 0
        posN = 0
        while posX < 63:
            # keep 1s in x
            while binaryX[posX] != 0 and posX < 63:
                posX += 1
            # replace 0s in x with bits in n-1
            binaryX[posX] = binaryN[posN]
            posX += 1
            posN += 1

        for i in range(64):
            if binaryX[i] == 1:
                ans += pow(2, i)

        return ans
