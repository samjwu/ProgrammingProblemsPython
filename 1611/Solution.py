class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        # 2 ^ exponent = MSB of n
        exponent = 0
        
        # to avoid changing n
        msb = 1
        
        while msb * 2 <= n:
            exponent += 1
            msb *= 2

        # number of operations to reach MSB from 0 = 2^(exp+1) - 1
        ops_to_msb = 2 ** (exponent + 1) - 1
        
        # recurse to get number of operations to reach (n - MSB) from 0
        ops_to_remainder = self.minimumOneBitOperations(n - msb)
        
        # num ops to reach n = num ops to reach MSB - num ops to reach remainder
        # why? max ops is to reach MSB. ops to "clean up" remainder can be skipped
        return ops_to_msb - ops_to_remainder
