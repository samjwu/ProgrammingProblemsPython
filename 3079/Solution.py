class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x: str) -> int:
            digit_count = len(x)
            high_digit = max(x)
            return int(high_digit * digit_count)

        encrypted_sum = 0

        for num in nums:
            encrypted_sum += encrypt(str(num))

        return encrypted_sum
