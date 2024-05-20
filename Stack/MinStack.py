class MinStack(object):

    def __init__(self):
        self.stack = []
        self.index = -1

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        d = self.index

        self.stack = [val] + self.stack
        self.index+=1
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(0)
        self.index-=1


        

    def top(self):
        """
        :rtype: int
        """
        d = self.index

        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()