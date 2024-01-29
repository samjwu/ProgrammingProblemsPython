class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        if len(self.stk2) > 0:
            return self.stk2.pop()
        
        while len(self.stk1) > 0:
            self.stk2.append(self.stk1.pop())
            
        return self.stk2.pop()

    def peek(self) -> int:
        if len(self.stk2) > 0:
            return self.stk2[-1]
        
        while len(self.stk1) > 0:
            self.stk2.append(self.stk1.pop())
            
        return self.stk2[-1]

    def empty(self) -> bool:
        return len(self.stk1) == 0 and len(self.stk2) == 0
