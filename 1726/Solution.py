class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        product_freq = {}

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]

                if product in product_freq:
                    product_freq[product] += 1
                else:
                    product_freq[product] = 1

        for freq in product_freq.values():
            # number of pairs is n * (n-1) / 2
            pairs = (freq * (freq - 1) // 2)

            # there are 8 arrangements for each pair of tuples
            ans += 8 * pairs

        return ans
