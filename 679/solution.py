class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def _can_form_24(cards: List[int]) -> bool:
            n = len(cards)

            # base case, only one card left
            # check if it is roughly 24
            if n == 1: 
                return abs(cards[0] - 24) < 1e-5

            # try all distinct number pairs
            for i in range(n):
                for j in range(i+1, n):
                    # create list of all remaining cards
                    # excluding the ith and jth cards being operated on
                    remaining_cards = [cards[k] for k in range(n) if k != i and k != j]

                    # try addition, both subtraction operations, and multiplication
                    operations = [
                        cards[i] + cards[j],
                        cards[i] - cards[j],
                        cards[j] - cards[i],
                        cards[i] * cards[j],
                    ]
                    # try both division operations, if not dividing by zero
                    if abs(cards[j]) > 1e-5:
                        operations.append(cards[i] / cards[j])
                    if abs(cards[i]) > 1e-5:
                        operations.append(cards[j] / cards[i])

                    for new_value in operations:
                        if _can_form_24(remaining_cards + [new_value]):
                            return True
                            
            # could not find any combination of operations that make 24
            return False

        return _can_form_24(cards)
