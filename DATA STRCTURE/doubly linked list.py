# DATA STRUDTURE\Thinking\
# doubly linked list

# Node of a Doubly Linked List
class Node(object): 
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None): 
        self.data = data 
        self.next = next 
        self.prev = prev 
        
    #method for setting the data field of the node 
    def setData(self,data): 
        self.data = data 
        
    #method for getting the data field of the node 
    def getData(self): 
        return self.data 
    
    #method for setting the next field of the node 
    def setNext(self,next): 
        self.next = next 
        
    #method for getting the next field of the node 
    def getNext(self): 
        return self.next 
    
    #returns true if the node points to another node 
    def hasNext(self):
        return self.next != None 
    
    #method for setting the next field of the node 
    def setPrev(self,prev): 
        self.prev = prev 
        
    #method for getting the next field of the node 
    def getPrev(self): 
        return self.prev 
    
    #returns true if the node points to another node 
    def hasPrev(self): 
        return self.prev != None 
    
    # __str__ returns string equivalent of Object 
    def __str__(self): 
        return "Node[Data = %s]" % (self.data,)
    
# Doubly linked list
class D_list(object):
    #constructor
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
        
    