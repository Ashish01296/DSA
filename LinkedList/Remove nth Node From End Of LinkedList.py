#Remove nth Node from End the LinkedList
def removeNthFromEnd(self, head, n):
    slow  =  fast = head


    #Traverse Fast pointer nth Node

    for i in range(n):
        fast = fast.next
    
    #Checking best case which n = 3 Linked list  is 1,2,3 then deleting nth node from last is 1
    if fast==None:
        return head.next
    
    
    while fast.next !=None:
        slow = slow.next
        fast = fast.next
    
    #Slow point to n-1 node and fast point to last node
    deleteNode = slow.next
    slow.next = slow.next.next
    deleteNode = None
    return head