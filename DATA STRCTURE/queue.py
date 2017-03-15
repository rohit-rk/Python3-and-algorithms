# DATA STRUDTURE\Thinking\
# queue - Array implementation

# Node of a Queue
class Queue(object):
    #constructor
    def __init__(self,limit = 5):
        self.q = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.size <= 0
    
    #To insert an element to rear of Queue
    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()
            
        self.q.append(item)
        
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Queue after enQueue : ", self.q)
    
    #To delete an element from front of Queue    
    def deQueue(self):
        if self.size <= 0:
            print("queue underfllow")
            return 0
        else:
            self.q.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
                
            print("Queue after deQueue: ",self.q)
            
    def queueRear(self):
        if self.rear is None:
            print("The Queue is empty")
            raise IndexError
        return self.q[self.rear]

    def queueFront(self):
        if self.front is None:
            print("The Queue is empty")
            raise IndexError
        return self.q[self.front] 
    
    def size(self):
        return self.size
    
    def resize(self):
        newQ = list(self.q)
        self.limit = 2*self.limit
        self.q = newQ
        
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


if __name__ == "__main__":
        main()
