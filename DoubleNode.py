class DoubleNode:
	
	def __init__(self,value):
		self.value = value
		self.nextnode = None
		self.prevnode = None

	def printNode(self):
        
        if self.nextnode and self.prevnode:
            
            print(self.prevnode.name,'[',self.prevnode.value,']','<---',self.name,'[',self.value,']','--->',self.nextnode.name,
                 '[',self.nextnode.value,']')
            
            if self.prevnode.nextnode == self and self.nextnode.prevnode == self:
                
                print(self.prevnode.name,'[',self.prevnode.value,']','--->',self.name,'[',self.value,']','<---',self.nextnode.name,
                 '[',self.nextnode.value,']')
                
            elif self.prevnode.nextnode == self:
                
                print(self.prevnode.name,'[',self.prevnode.value,']','--->',self.name,'[',self.value,']')
                
            elif self.nextnode.prevnode == self:
                
                print(self.name,'[',self.value,']','<---',self.nextnode.name,
                 '[',self.nextnode.value,']')
                
        elif self.prevnode:
            
            print(self.prevnode.name,'[',self.prevnode.value,']','<----',self.name,'[',self.value,']','--->',None)
            if self.prevnode.nextnode == self:
                print(self.prevnode.name,'[',self.prevnode.value,']','--->',self.name,'[',self.value,']')
            
        elif self.nextnode:
            
            print(self.name,'[',self.value,']','--->',self.nextnode.name,'[',self.nextnode.value,']')
            if self.nextnode.prevnode == self:
                print(self.name,'[',self.value,']','<---',self.nextnode.name,'[',self.nextnode.value,']')
            
            for x in DoubleNode.available_nodes:
                if x.nextnode == self:
                    print(x.name,'[',x.value,']','--->',self.name,'[',self.value,']')
            
        else:
            for x in DoubleNode.available_nodes:
                if x.nextnode == self:
                     print(x.name,'[',x.value,']','--->',self.name,'[',self.value,']')
                        
                if x.prevnode == self:
                    print(self.name,'[',self.value,']','<---',x.name,'[',x.value,']')
                
            print('This node {} is not pointing to any other nodes'.format(self.name))
            