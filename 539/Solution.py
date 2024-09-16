class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)

        totalMin = []

        for time in timePoints:
            hours = int(time[:2])
            minutes = int(time[3:])
            totalMin.append(hours * 60 + minutes)

        totalMin.sort()

        ans = float("inf")

        for i in range(n-1):
            ans = min(ans, totalMin[i+1] - totalMin[i])

        ans = min(ans, 24 * 60 - totalMin[-1] + totalMin[0])
        
        return ans
