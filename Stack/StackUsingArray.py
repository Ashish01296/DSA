#Stack using array/List...


#Last in first out..
class stack:
    def __init__(self):
        self.values = []
    

    def push(self,x):
        self.values = [x] + self.values
    
    def pop(self):
        return self.values.pop(0)
    

    def top(self):
        return self.values[0]
    

    def isEmpty(self):
        if self.values==None:
            return True
        else:
            return False





s= stack()


s.push(10)
s.push(20)
s.push(30)
s.pop()


print(s.values)
print(s.top())
print(s.isEmpty())