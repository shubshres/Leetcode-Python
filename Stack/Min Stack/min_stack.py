class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    # pushes element onto stack
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            val = min(val, self.minStack[-1])

        self.minStack.append(val)

    # pops element on the top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # gets the minimum
    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
