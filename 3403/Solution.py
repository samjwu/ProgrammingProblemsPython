class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        lex_largest = ""

        for i in range(n):
            # max len substr has length = n - numFriends + 1
            substring = word[i : min(i + n - numFriends + 1, n)]
            lex_largest = max(lex_largest, substring)

        return lex_largest
