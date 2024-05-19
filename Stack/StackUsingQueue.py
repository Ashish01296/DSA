# Implement Stack using Queues

class MyStack(object):

    def __init__(self):
        self.num = []
        self.index = -1
        

    def push(self, x):
        self.num.append(x)
        self.index+=1        

    def pop(self):
        d = self.index
        val = self.num.pop(d)
        self.index-=1
        return val


    def top(self):
        d = self.index
        return self.num[d]
        

    def empty(self):
        return self.index == -1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()