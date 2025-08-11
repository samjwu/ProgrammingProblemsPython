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

        query_products = []

        for left, right in queries:
            curr_product = 1
            # multiply 1 by everything in the bounds of the query
            for i in range(left, right + 1):
                curr_product = curr_product * n_powers[i] % MOD
            query_products.append(curr_product)

        return query_products
