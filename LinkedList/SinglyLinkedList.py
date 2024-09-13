'''
1. Create Node

2. Create class to Linked the Node...
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None



    #Traversing the Linked list

    def print_ll(self):
        n = self.head

        if self.head is None:
            print("Linked List is Empty.")
        

        while n is not None:
            print(n.data,end="->")
            n = n.next


    #Adding element at begging

    def add_begin(self,data):
        n = self.head

        new_node = Node(data)
        new_node.next = n
        self.head = new_node


    #Adding element at the end

    def add_end(self,data):
        n = self.head

        new_node = Node(data)

        while n.next is not None:
            n = n.next
        n.next = new_node


    #Adding element at the Specific Node..

    def given_node(self,data,TargetNode):
        n = self.head

        while n is not None:
            if n.data == TargetNode:
                break
            n = n.next

        if n is None:
            print("Node is not Present in the Linked List")
        else:
            print("Node is Present in the Linked List")
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
    

    def delte_begin(self):

        if self.head==None:
            print("LL is empty")
        
        else:
            n = self.head
            self.head = n.next


 
    
           
           

    
           








l = LinkedList()


l.add_begin(30)
l.add_begin(20)
l.add_begin(10)
l.add_end(40)
l.add_end(60)
l.given_node(50,40)

l.delte_begin()


l.print_ll()


