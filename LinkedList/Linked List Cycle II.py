# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

            # if cycle found then Reset to slow pointer to the head 
            if slow==fast:
                slow = head

                  #Unitil we don't found cycle we have to move our slow and fast pointer by one.. and return slow
                while slow!=fast:
                    slow =slow.next
                    fast= fast.next
                return slow
        #If no cycle found then return None
        return None

           
           
        
