# Last in First out LIFO

class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return 'Stack is Empty'
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    