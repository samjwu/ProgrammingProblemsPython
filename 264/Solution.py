class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglySet = set()
        
        uglySet.add(1)

        currUgly = 1

        for i in range(n):
            currUgly = min(uglySet)
            uglySet.remove(currUgly)

            uglySet.add(currUgly * 2)
            uglySet.add(currUgly * 3)
            uglySet.add(currUgly * 5)

        return currUgly
