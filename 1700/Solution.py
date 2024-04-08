class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        
        food = deque(sandwiches)
        
        while len(q) > 0 and len(food) > 0:
            taken = False
            
            for i in range(len(q)):
                if len(food) == 0:
                    break
                    
                nextStudent = q.popleft()
                
                if nextStudent == food[0]:
                    food.popleft()
                    taken = True
                else:
                    q.append(nextStudent)
            
            if taken == False:
                break
            
        return len(q)
