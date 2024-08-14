class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        hi = nums[-1]

        maxDist = hi*2

        # prefixes[i] = freq of values <= i
        prefixes = [0 for i in range(maxDist)]
        index = 0
        for value in range(maxDist):
            while index < n and nums[index] <= value:
                index += 1
            prefixes[value] = index

        # valFreq[i] = count of nums with value i
        valFreq = [0 for i in range(hi+1)]
        for i in range(n):
            valFreq[nums[i]] += 1

        # binary search
        left = 0
        right = hi
        while left < right:
            mid = (left + right) // 2

            # count number of pairs with dist <= mid
            count = self.countPairs(nums, prefixes, valFreq, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def countPairs(self, nums: List[int], prefixes: List[int], valFreq: List[int], dist: int) -> int:
        count = 0

        n = len(nums)
        
        index = 0

        while index < n:
            currVal = nums[index]

            currCount = valFreq[currVal]

            # number of values larger than current value within dist

            # prefixes[min(currVal + dist, len(prefixes) - 1)]
            # gives the total count of elements that are less than or equal to current value + dist.
            largerCount = prefixes[min(currVal + dist, len(prefixes) - 1)] - prefixes[currVal]

            # number of pairs with same value
            sameCount = currCount * (currCount - 1) // 2

            # total number of valid pairs equals
            # number of pairs using current value and larger values
            # plus number of pairs using current value
            count += largerCount * currCount + sameCount

            # skip duplicate values
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1

            index += 1

        return count
