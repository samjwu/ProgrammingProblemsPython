class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        lowerBound = 0
        upperBound = 1
        
        while True:
            # midpoint of search space
            midFraction = (lowerBound + upperBound) / 2
            
            # calc counts of elements less than arr[i] / midFraction
            fractionCounts = [bisect.bisect(arr, arr[i] / midFraction) for i in range(n)]
            
            # calc total count of fractions less than midFraction
            countOfSmallerFractions = sum(n - i for i in fractionCounts)

            if countOfSmallerFractions > k:
                upperBound = midFraction
            elif countOfSmallerFractions < k:
                lowerBound = midFraction
            else:
                # since countOfSmallerFractions == k,
                # highest fraction in fractionCounts is answer
                return max([(arr[i], arr[j]) for i, j in enumerate(fractionCounts) if j < n], key=lambda x: x[0] / x[1])
