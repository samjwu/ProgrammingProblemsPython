class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def calc_num_bits(num) -> int:
            bits = 0
            
            while num:
                if num & 1:
                    bits += 1
                num >>= 1
                
            return bits
        
        # sort by num bits asc, then by num in asc order if num bits is tied
        arr.sort(key = lambda num: (calc_num_bits(num), num))
        
        return arr
