class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        input_freq = defaultdict(int)
        ans = []

        for digit in digits:
            input_freq[digit] += 1
        
        # skip 2 for even
        for num in range(100, 999, 2):
            # check digit freq in candidate number
            candidate_freq = defaultdict(int)
            for digit in str(num):
                candidate_freq[int(digit)] += 1
            
            is_valid = True
            for digit in candidate_freq:
                if digit not in input_freq or candidate_freq[digit] > input_freq[digit]:
                    is_valid = False
                    break

            if is_valid:
                ans.append(num)
        
        return ans
