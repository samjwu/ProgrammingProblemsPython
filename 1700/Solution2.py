class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefer0 = 0
        
        prefer1 = 0
        
        for student in students:
            if student == 0:
                prefer0 += 1
            else:
                prefer1 += 1
        
        for sandwich in sandwiches:
            if sandwich == 0 and prefer0 == 0:
                return prefer1
            
            if sandwich == 1 and prefer1 == 0:
                return prefer0
            
            if sandwich == 0:
                prefer0 -= 1
            else:
                prefer1 -= 1
                
        return 0
