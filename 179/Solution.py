class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = []

        for num in nums:
            strs.append(str(num))

        # concat string with itself 10 times and sort in reverse lexicographical order
        strs.sort(key=lambda a: a * 10, reverse=True)

        if strs[0] == "0":
            return "0"

        return "".join(strs)
