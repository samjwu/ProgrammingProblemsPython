class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # flip counter
        q = deque()

        for i in range(n):
            # shrink flip counter for flips outside window of 3
            while q and q[0] < i - 2:
                q.popleft()

            # check current value at i, plus past flips at i
            # length of flip counter equals past flips at i
            if (nums[i] + len(q)) % 2 == 0:
                # need to flip window of 3
                if i + 2 >= n:
                    return -1

                ans += 1

                # expand flip counter
                q.append(i)

        return ans
