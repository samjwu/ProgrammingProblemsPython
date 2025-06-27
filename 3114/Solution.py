class Solution:
    def findLatestTime(self, s: str) -> str:
        latest_time = ""

        for i in range(12):
            for j in range(60):
                left = str(i).zfill(2)
                right = str(j).zfill(2)
                t = left + ":" + right

                if all(s[i] == t[i] or s[i] == '?' for i in range(5)):
                    latest_time = t

        return latest_time                       
