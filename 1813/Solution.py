class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deque1 = deque(sentence1.split())
        deque2 = deque(sentence2.split())

        # remove common prefix
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.popleft()
            deque2.popleft()

        # remove common suffix
        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop()
            deque2.pop()

        # valid answer if one sentence is empty
        return not deque1 or not deque2
