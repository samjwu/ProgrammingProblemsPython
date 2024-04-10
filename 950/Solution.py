class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        ans = deque()

        for card in deck[::-1]:
            ans.rotate()
            ans.appendleft(card)

        return list(ans)
