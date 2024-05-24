class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.ans = 0

        n = len(words)

        takenLetters = [0 for i in range(26)]
        
        haveLetters = [0 for i in range(26)]
        for letter in letters:
            haveLetters[ord(letter) - ord("a")] += 1

        def canTakeWord(takenLetters: List[int]) -> bool:
            for i in range(26):
                if haveLetters[i] < takenLetters[i]:
                    return False
            else:
                return True
        
        def recurse(idx: int, words: List[str], score: int, takenLetters: List[int], totalScore: int):
            # checked all words
            if idx == -1:
                # compare score of current set to max
                self.ans = max(self.ans, totalScore)
                return

            # calc score without words[idx]
            recurse(idx - 1, words, score, takenLetters, totalScore)

            # calc score with words[idx]
            wordLen = len(words[idx])
            for i in range(wordLen):
                c = ord(words[idx][i]) - ord("a")
                takenLetters[c] += 1
                totalScore += score[c]

            # only consider score with words[idx] if it is possible
            if canTakeWord(takenLetters):
                recurse(idx - 1, words, score, takenLetters, totalScore)
                
            # backtrack
            for i in range(wordLen):
                c = ord(words[idx][i]) - ord("a")
                takenLetters[c] -= 1
                totalScore -= score[c]

        recurse(n - 1, words, score, takenLetters, 0)

        return self.ans
