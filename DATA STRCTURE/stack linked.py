# DATA STRUDTURE\Thinking\
# stack - Linked list implementation

# Node of a Singly linked list
class Node(object): 
    #constructor 
    def __init__(self, data=None): 
        self.data = data
        self.next = None 
        
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


class Stack(object):
    #constructor
    def __init__(self, data = None):
        self.top = None
        if data:
            for data in data:
                self.push(data)
    
    #To insert an element into Stack
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.top)
        self.top = temp

    #To delete an Top element from Stack
    def pop(self):
        if self.top is None:
            raise IndexError 
        temp = self.top.getData()
        self.top = self.top.getNext()
        return temp
    
    #To display the top Element
    def peek(self):
        if self.top is None:
            raise IndexError
        return self.top.getData()
    
    #Display Stack starting from top  
    def displayList(self):
        print("Stack : ",)       
        if self.top != None:
            current = self.top 
        
            while(current != None):
                print(current.getData(),end = " ")
                current = current.getNext()
        else:
            print("Empty list")       


def main():
    list = ["first","second","third"]
    s1 = Stack(list)
    s1.push("1")
    s1.push("21")
    s1.push("14")
    s1.push("31")
    s1.push("19")
    s1.push("3")
    s1.push("99")
    s1.push("9")
    print(s1.peek())
    print(s1.pop())
    print(s1.peek())
    print(s1.pop())
    s1.displayList()
    print(" ")
    print(s1.pop())
    
if __name__ == "__main__":
    main()