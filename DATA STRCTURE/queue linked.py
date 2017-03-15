# DATA STRUDTURE\Thinking\
# queue - Queue implementation

# Node of a Singly Linked List 
class Node(object): 
    #constructor 
    def __init__(self, data=None, next=None): 
        self.data = data
        self.last = None
        self.next = next
        
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
    
    #method for setting the next field of the node 
    def setLast(self,last): 
            self.last = last 
            
    #method for getting the next field of the node 
    def getLast(self):
        return self.last   
    
    #returns true if the node points to another node 
    def hasNext(self): 
        return self.next != None

# Node of a Queue
class Queue(object):
    #constructor
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0
        
    #To insert an element to front of Queue
    def enQueue(self,data):
        lastNode = self.front
        self.front =  Node(data,self.front)
        if lastNode:
            lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
            
        self.size += 1
        
    def queueRear(self):
        if self.rear is None:
            print("The Queue is empty.")
            raise IndexError
        return self.rear.getData()
    
    def queueFront(self):
        if self.front is None:
            print("The Queue is empty.")
            raise IndexError
        return self.front.getData()
    
    #To delete an element from rear of Queue 
    def deQueue(self):
        if self.front is None:
            print("The Queue is empty.")
            raise IndexError
        result = self.rear.getData()
        self.rear = self.rear.last
        self.rear.next = None
        self.size -= 1
        return result
    
    def size(self):
        return self.size
    
    #Display Stack starting from top  
    def displayList(self):
        print("Queue : ",)       
        if self.front != None:
            current = self.front 
        
            while(current != None):
                print(current.getData(),end = " ")
                current = current.getNext()
        else:
            print("Empty list")        
        
def main():
    q = Queue()
    
    q.enQueue("first")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())

    q.enQueue("second")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())    

    q.enQueue("third")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())    

    q.enQueue("four")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())        

    q.enQueue("five")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())    
    
    q.enQueue("six")
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())     

    q.deQueue()
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())    

    q.deQueue()
    print("Front: "+q.queueFront())
    print("Rear: "+q.queueRear())    
    
    q.displayList()
    print(" ")
    print(q.deQueue())    
    q.displayList()

if __name__ == "__main__":
            main()
