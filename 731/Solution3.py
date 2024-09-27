class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # conflict with existing overlap = triple booking
        for overlap in self.overlaps:
            if self.overlapped(overlap[0], overlap[1], start, end):
                return False
            
        for booking in self.calendar:
            if self.overlapped(booking[0], booking[1], start, end):
                self.overlaps.append(self.calcInterval(booking[0], booking[1], start, end))
                
        self.calendar.append((start, end))
        
        return True
    
    def overlapped(self, s1: int, e1: int, s2: int, e2: int) -> bool:
        return max(s1, s2) < min(e1, e2)

    def calcInterval(self, s1: int, e1: int, s2: int, e2: int) -> list[int]:
        return [max(s1, s2), min(e1, e2)]
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
