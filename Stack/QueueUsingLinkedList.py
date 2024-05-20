class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
    

    def is_Empty(self):
        if self.head==None:
            return True
    

    def Enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
          
            self.head = new_node
        
        else:
            n = self.head
            while n.next!=None:
                n = n.next
            n.next = new_node

    def PrintQueue(self):
        n = self.head

        while n!=None:
            print(n.data,end="->")
            n = n.next
    

    def front(self):
        return self.head.data
    

    def rear(self):

        n = self.head

        while n.next!=None:
            n = n.next
        
        return n.data
    

    def Dequeue(self):
        if self.head==None:
            return -1
        
        else:
            self.head = self.head.next




q = Queue()

q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)

q.Dequeue()
print(q.front())
print(q.rear())

q.PrintQueue()


