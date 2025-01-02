class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowelStr(word):
            vowel = set("aeiou")
            return word[0] in vowel and word[-1] in vowel

        def constructPrefix(words):
            prefix = {}
            runningSum = 0

            for i in range(len(words)):
                runningSum += isVowelStr(words[i])
                prefix[i] = runningSum

            return prefix

        prefixSum = constructPrefix(words)

        ans = []

        for l, r in queries:
            if l > 0:
                ans.append(prefixSum[r] - prefixSum[l-1])
            else:
                ans.append(prefixSum[r])

        return ans
