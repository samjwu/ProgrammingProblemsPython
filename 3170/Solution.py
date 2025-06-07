class Solution:
    def clearStars(self, s: str) -> str:
        # use stacks for each letter
        stacks = [[] for i in range(26)]
        arr = list(s)

        for i, c in enumerate(arr):
            if c != "*":
                stacks[ord(c) - ord("a")].append(i)
            else:
                # go from lex small to large
                for j in range(26):
                    if stacks[j]:
                        # removing the rightmost lex small char results in lex smallest string
                        arr[stacks[j].pop()] = "*"
                        break

        return "".join(c for c in arr if c != "*")
