from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        # store the powers of two that add up to n
        n_powers = []
        # 2^0
        curr_power = 1
        # find the powers of two that add up to n
        while n > 0:
            if n % 2 == 1:
                n_powers.append(curr_power)
            n //= 2
            curr_power *= 2

        # m is at most 32 for 32-bit number
        m = len(n_powers)
        # precompute the values to make query lookups O(1)
        # product_ranges[i][j] = product from index i to j
        product_ranges = [[0 for j in range(m)] for i in range(m)]
        product_ranges = {}
        for i in range(m):
            curr_product = 1
            for j in range(i, m):
                curr_product = curr_product * n_powers[j] % MOD
                product_ranges[(i, j)] = curr_product

        query_products = []
        for left, right in queries:
            query_products.append(product_ranges[(left, right)])
        return query_products
