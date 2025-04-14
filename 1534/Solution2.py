class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        # prefix_count[x] = number of elements <= x
        prefix_count = [0] * 1001
        
        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    # if |arr[i] - arr[j]| <= a
                    # then arr[i] is in [arr[j] - a, arr[j] + a]
                    lj = arr[j] - a
                    rj = arr[j] + a
                    
                    # if |arr[i] - arr[k]| <= c
                    # then arr[i] is in [arr[k] - c, arr[k] + c]
                    lk = arr[k] - c
                    rk = arr[k] + c
                    
                    # find the tightest bounds from the two bounds above
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)

                    if l <= r:
                        ans += prefix_count[r]
                        if l > 0:
                            ans -= prefix_count[l-1]

            for k in range(arr[j], 1001):
                prefix_count[k] += 1

        return ans
