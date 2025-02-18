class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.ans = []

        self.generateString(0, 0, pattern)
        
        return "".join(self.ans[::-1])

    def generateString(self, idx: int, number: int, pattern: str) -> int:
        if idx != len(pattern):
            if pattern[idx] == "I":
                self.generateString(idx + 1, idx + 1, pattern)
            else:
                number = self.generateString(idx + 1, number, pattern)

        self.ans.append(str(number + 1))

        return number + 1
