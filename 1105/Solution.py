class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        self.n = len(books)

        memo = [[0 for j in range(shelfWidth + 1)] for i in range(self.n)]

        return self.recurse(books, shelfWidth, memo, 0, shelfWidth, 0)

    def recurse(self, books: List[List[int]], shelfWidth: int, memo: List[List[int]], i: int, remainingWidth: int, maxHeight: int) -> int:
        currBook = books[i]

        # check if current book is tallest for current shelf
        candidateMaxHeight = max(maxHeight, currBook[1])

        # last book
        if i == self.n - 1:
            # try to place on current shelf
            if remainingWidth >= currBook[0]:
                return candidateMaxHeight

            # otherwise make new shelf
            return maxHeight + currBook[1]

        if memo[i][remainingWidth] != 0:
            return memo[i][remainingWidth]

        # try to place on new shelf
        newShelfHeight = maxHeight + self.recurse(
            books,
            shelfWidth,
            memo,
            i + 1,
            shelfWidth - currBook[0],
            currBook[1],
        )

        # try to place on current shelf
        if remainingWidth >= currBook[0]:
            currShelfHeight = self.recurse(
                books,
                shelfWidth,
                memo,
                i + 1,
                remainingWidth - currBook[0],
                candidateMaxHeight,
            )
            
            # take min of two results
            memo[i][remainingWidth] = min(newShelfHeight, currShelfHeight)
            return memo[i][remainingWidth]

        # can only place on new shelf
        memo[i][remainingWidth] = newShelfHeight
        return memo[i][remainingWidth]
