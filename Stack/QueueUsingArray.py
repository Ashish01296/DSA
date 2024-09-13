

#First in first out...

class Queue:
    def __init__(self):
        self.values = []
    

    def enQueue(self,x):
        self.values.append(x)
    

    def deQueue(self):
        return self.values.pop(0)
    

    def front(self):
        return self.values[0]
    
    def rear(self):
        d = len(self.values) - 1
        return self.values[d]
    

    def isEmpty(self):
        if self.values==None:
            return True
        else:
            return False


    def Size(self):
        return len(self.values)
    
    def reverse(self):
        return(self.values.reverse())




Q  = Queue()

Q.enQueue(10)
Q.enQueue(20)
Q.enQueue(30)
Q.deQueue()




print(Q.values)
print(Q.front())
print(Q.rear())
print(Q.Size())
print(Q.isEmpty())


