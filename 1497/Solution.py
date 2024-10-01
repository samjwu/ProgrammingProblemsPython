class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = defaultdict(int)
        
        for num in arr:
            rem = num % k
            # handle negative num
            if rem < 0:
                rem = (rem + k) % k
                
            remainders[rem] += 1
            
        for num in arr:
            rem = num % k
            # handle negative num
            if rem < 0:
                rem = (rem + k) % k
            
            if rem == 0:
                if remainders[rem] % 2 == 1:
                    return False
            elif remainders[rem] != remainders[k - rem]:
                return False
            
        return True
