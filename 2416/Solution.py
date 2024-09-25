class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            idx = ord(c) - ord("a")

            # create new node for unseen prefixes
            if node.next[idx] is None:
                node.next[idx] = TrieNode()

            # count the prefix
            node.next[idx].count += 1

            node = node.next[idx]

    def count(self, word: str) -> int:
        node = self.root

        ans = 0
        
        for c in word:
            idx = ord(c) - ord("a")
            ans += node.next[idx].count
            node = node.next[idx]

        return ans

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)

        # construct trie
        for i in range(n):
            self.insert(words[i])
            
        ans = [0] * n

        # count all prefixes in each string
        for i in range(n):
            ans[i] = self.count(words[i])

        return ans
