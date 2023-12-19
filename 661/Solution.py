class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        ans = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        total += img[x][y]
                        count += 1

                ans[i][j] = total // count
        
        return ans
