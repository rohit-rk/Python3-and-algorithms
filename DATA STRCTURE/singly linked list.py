# DATA STRUDTURE\Thinking\
# singly linked list

# Node of a Singly Linked List 
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
    
    
# Singly Linked list
class S_list(object):
    #constructor
    def __init__(self):
        self.head = None
        self.length = 0
        
    #length of linked list
    def listLength(self):
        return self.length
    
    #Inserting a node at the beginning
    def insertAtBeg(self, data):
        newNode = Node(data)
        
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
            
        self.length += 1
    
    #Inserting a node at the end
    def insertAtEnd(self, data):
        newNode = Node(data)
        current = self.head
         
        while current.getNext() != None:
            current = current.getNext()
        
        current.setNext(newNode)
        self.length += 1
    
    #Insert a Node at any position
    def insertAtpos(self, pos, data):
        pos -= 1
        if pos > self.length or pos < 0:
            print("Insertion at wrong position")
            return None
        else:
            if pos == 0:
                self.insertAtBeg(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node(data)
                    current = self.head
                    count = 1
                    
                    while(count < pos-1):
                        count += 1
                        current = current.getNext()
                        
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1
                
    #Delete the first node of the linked list 
    def deleteFromBeg(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1
            
    #Delete the last node of the linked list
    def deleteFromLast(self):
        if self.length == 0:
            print('The list is empty')
        else:
            current = self.head
            previous = current
            
            while current.getNext() != None:
                previous = current
                current = current.getNext()
                
            previous.setNext(None)
            self.length -= 1
            
    #Delete a node at a particular position
    def deleteFromPos(self, pos):
        count = 0
        current = self.head
        previous = None
        if pos > self.length or pos <= 0:
            print("The position does not exist. Please enter a valid position.")
        elif pos == 1:
            self.deleteFromBeg()
        elif pos == self.length:
            self.deleteFromLast()
        else:
            while current.getNext() != None:
                count += 1
                if count == pos:
                    previous.setNext(current.getNext())
                    self.length -= 1
                    return
                else:
                    previous = current 
                    current = current.getNext()
    #Delete with data from linked list
    def deleteValue(self,value):
        current = self.head
        previous = None
        
        while current != None:
            if current.getData() == value:                
                if previous == None:
                    self.deleteFromBeg()
                    return
                else:
                    previous.setNext(current.getNext())
                    self.length -= 1
                    return
            else:
                previous = current
                current = current.getNext()
        print("The value provided is not present.")
        
    #Delete singly linked list
    def clear(self):
        self.head = None
        
    #Traverse the list    
    def displayList(self):
        if self.head != None:
            current = self.head 
            count = 0
    
            while(current != None):
                count += 1
                print("The data of linked list at position %d is : %d" \
                      %(count,current.getData()))
                current = current.getNext()
        else:
            print("Empty list")
                

# Main
def main():
    '''Main Function'''
    print("\t\t\tSINGLY LINKED LIST")
    choice = 0
    list = S_list()
    
    while 1:
        print("0.To Exit")
        print("1.Insert data at start.")
        print("2.Insert data at end.")
        print("3.Insert data at any position.")
        print("4.Delete data from start.")
        print("5.Delete data from end.")
        print("6.Delete data from any position.")
        print("7.Delete data by it's value.")
        print("8.Show size of Linked List.")
        print("9.Display Linked List.")
        print("10.To delete the whole Linked List.")
        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                list.insertAtBeg(int(input("Enter data to be inserted: ")))
            elif choice == 2:
                list.insertAtEnd(int(input("Enter data to be inserted: ")))
            elif choice == 3:
                a = int(input("Enter the positiion of data to be inserted:"))
                b = int(input("Enter the data:"))
                list.insertAtpos(a,b)
            elif choice == 4:
                list.deleteFromBeg()
            elif choice == 5:
                list.deleteFromLast()
            elif choice == 6:
                list.deleteFromPos(int(input("Enter the position of node to be deleted:")))
            elif choice == 7:
                list.deleteValue(int(input("Enter the value to be deleted:")))          
            elif choice == 8:
                print("The size of linked list is : " + str(list.listLength()))          
            elif choice == 9:
                list.displayList()          
            elif choice == 10:
                list.clear()
            elif choice == 0:
                            break             
            else:
                print("Invalid Input")
        except Exception as e:
            print("Error ocurred ")
            print("Error message: " + str(e))    
    
    
if __name__ == '__main__':
    main()         