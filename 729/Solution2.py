class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for book in self.calendar:
            if book[1] > start and end > book[0]:
                return False
            
        self.calendar.append((start, end))
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
