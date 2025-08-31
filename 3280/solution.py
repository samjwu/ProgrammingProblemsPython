class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = date.split("-")
        binary = [str(bin(int(num)))[2:] for num in nums]
        return "-".join(binary)
