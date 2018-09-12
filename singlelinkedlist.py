class Node:

    def __init__(self,value):
        self.value = value
        self.nextnode = None


    def loopCheck(self):
        # checking if the linked list is looped

        marker1 = self
        marker2 = self

        while marker2 != None and marker2.nextnode != None:
            marker1 = marker1.nextnode
            marker2 = marker2.nextnode.nextnode

            if marker2 == marker1:
                return True

        return False


    def reverse(self):
        # reverse the linked list assuming our node is the head of the list

        current = self
        previous = None
        nextnode = None

        while current:
            
            nextnode = current.nextnode
            current.nextnode = previous
            previous = current
            current = nextnode

        return previous

    def Kth_to_last_element(self,k):
        #getting the value of the Kth to the last element assuming our node
        # is the head of the list

        left_pointer = self
        right_pointer = self

        for i in range(k-1):

            if not right_pointer.nextnode:
                raise LookupError('Error: k is the larger than the list')

            right_pointer = right_pointer.nextnode

        while right_pointer.nextnode:

            left_pointer = left_pointer.nextnode
            right_pointer = right_pointer.nextnode

        return left_pointer.value

    def deleteNode(self,n):
        # deleting a node n from the linked list assuming our node is the head

        if self == n:
        self.nextnode = None
        self = None
        return 'Deleted the head node {}'.format(self.name)
    
        if n.nextnode == None:
            while self.nextnode:
                if self.nextnode == n:
                    self.nextnode = None
                    break
                self = self.nextnode
            return 'Node {} has been deleted'.format(n.name)
    
        while self.nextnode:
            if self.nextnode == n:
                temp = self.nextnode.nextnode
                n.nextnode = None
                self.nextnode = temp
                    
            self = self.nextnode
        
    
        return ' Node {} has been deleted'.format(n.name) 

        