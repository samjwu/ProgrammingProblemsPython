class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        elif a == b and b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isosceles"
        else:
            return "scalene"
