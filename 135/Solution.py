from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for i in range(n)]
        
        for i in range(n):
            self.assign_candy(ratings, candies, i, n)
        
        for i in range(n-1, -1, -1):
            self.assign_candy(ratings, candies, i, n)
        
        return sum(candies)
    
    def assign_candy(self, ratings: List[int], candies: List[int], i: int, n: int) -> None:
        rated_higher_than_prev = i > 0 and ratings[i] > ratings[i-1]
        rated_higher_than_next = i < n-1 and ratings[i] > ratings[i+1]

        if rated_higher_than_prev and rated_higher_than_next:
            candies[i] = max(candies[i-1], candies[i+1]) + 1
        elif rated_higher_than_prev:
            candies[i] = candies[i-1] + 1
        elif rated_higher_than_next:
            candies[i] = candies[i+1] + 1
