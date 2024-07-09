class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        
        foodReadyTime = 0
        totalWait = 0
        
        for customer in customers:
            startTime = customer[0]
            prepTime = customer[1]

            foodReadyTime = max(foodReadyTime, startTime) + prepTime
            
            totalWait += foodReadyTime - startTime
            
        return totalWait / n
