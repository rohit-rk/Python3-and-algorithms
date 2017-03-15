# DATA STRUDTURE\Thinking\
# stack - Array implementation

# Node of a Stack
class Stack(object):
    #constructor    
    def __init__(self,limit):
        self.stk = []
        self.limit = limit
        
    def isEmppty(self):
        return len(self.stk) <= 0
    
    #To insert an element into Stack
    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
            
        self.stk.append(item)
        print("Stack after Push :", self.stk)
    
    #To delete an Top element from Stack
    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:
            return self.stk.pop()
    #To display the top Element
    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow")
            return 0
        else:
            return self.stk[-1]
        
    def size(self):
        return len(self.stk)
    
    def resize(self):
        newStack = list(self.stk)
        self.limit = 2*self.limit
        self.stk = newStack
    
def main():
    s1 = Stack(5)
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
    
    
    
if __name__ == "__main__":
    main()

        
        