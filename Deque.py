class Deque:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return 'Deque is Empty'
    
    def removeRear(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return 'Deque is Empty'
    
    def size(self):
        return len(self.items)
    