class MinStack:

    def __init__(self):
        self.st=[]
        self.mst=[]
    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mst:
            self.mst.append(value)
        else:
            self.mst.append(min(self.mst[-1],value))
        
    def pop(self) -> None:
        self.st.pop()
        self.mst.pop()
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
