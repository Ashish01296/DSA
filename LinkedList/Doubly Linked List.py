class Node:
    def __init__(self,data):
        self.prev = None
        self.data= data
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
    

    def add_begin(self,data):

        n = self.head

        if self.head==None:
            self.head = Node(data)
        
        else:
            new_node = Node(data)
            new_node.next = n
            n.prev = new_node
            self.head = new_node
    

    def printLL(self):

        if self.head is None:
            print("Doubly Linked list is Empty")
        
        else:
            n = self.head

            while n!=None:
                print(n.data,end="->")
                n = n.next
    

    def add_end(self,data):

        n = self.head

        new_node = Node(data)

        while n.next is not None:
            n = n.next
        n.next = new_node
    

    def begin_del(self):

        if self.head==None:
            print("Can't delete bcz Linked list is Empty")
        
        else:
            n = self.head
            self.head = n.next
        
    


n  = DoublyLinkedList()

n.add_begin(10)
n.add_begin(20)
n.add_end(30)
n.begin_del()
n.printLL()


