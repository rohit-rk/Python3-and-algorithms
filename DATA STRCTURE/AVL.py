# DATA STRUDTURE\Thinking\
# AVL - Adelson-Velskii and Landis Trees

# Node of a Adelson-Velskii and Landis Tree
class AVLNode(object):
    #constructor
    def __init__(self,data,balance = 0,left = None,right = None):
        self.data = data
        self.balance = balance
        self.left = left
        self.right = right
        
    def setData(self,data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getBalance(self):
            return self.balance   

class AVLTree(object):
    #constructor
    def __init__(self):
        self.root = None
        
    def inOrderPrint(self):
        self.recInOrder(self.root)
        
    def recInOrder(self,root):
        if root != None:
            self.recInOrder(root.left)
            print(root.data)
            self.recInOrder(root.right)
            
    def insert(self,data):
        newNode = AVLNode(data)
        [self.root,taller] = self.recInsertAVL(self.root, newNode)
        
    def recInsertAVL(self,root,newNode):
        if root == None:
            root = newNode
            root.balance = 0
            taller = True
        elif newNode.data < root.data:
            [root.left,taller] = self.recInsertAVL(root.left, newNode)
            if taller:
                if root.balance == 0:
                    root.balance = -1
                elif root.balance == 1:
                    root.balance = 0
                    taller = False
                else:
                    root = self.leftRightRotate(root)
                    taller = False
        else:
            [root.right, taller] = self.recInsertAVL(root.right, newNode)
            if taller:
                if root.balance == -1:
                    root.balance = 0
                    taller = False
                elif root.balance == 0:
                    root.balance = 1
                else:
                    root = self.rightLeftRotate(root)
                    taller = False
        return [root, taller]
    def rightLeftRotate(self,root):
        X = root.right
        if X.balance == 1:
            root.balance = 0
            X.balance = 0
            root = self.singleRightRotate(root)
        else:
            Y = X.left
            if Y.balance == -1:
                root.balance = 0
                X.balance = 1
            elif Y.balance == 0:
                root.balance = 0
                X.balance = 0
            else:
                root.balance = -1
                X.balance = 0
            Y.balance = 0
            root.right = self.singleLeftRotate(X)
            root = self.singleRightRotate(root)
            return root
    
    def leftRightRotate(self,root):
        X = root.left
        if X.balance == -1:
            root.balance = 0
            X.balance = 0
            root = self.singleLeftRotate(root)
        else:
            Y = X.right
            if Y.balance == -1:
                root.balance = 1
                X.balance = 0
            elif Y.balance == 0:
                root.balance = 0
                X.balance = 0
            else:
                root.balance = 0
                X.balance = -1
            Y.balance = 0
            root.left = self.singleRightRotate(X)
            root = self.singleLeftRotate(root)
        return root
    
    
    def singleRightRotate(self,root):
        X = root.right
        root.right = X.left
        X.left = root
        return X

    def singleLeftRotate(self,root):
        X = root.left
        root.left = X.right
        X.right = root
        return X    
    
    def height(self):
        return self.recHeight(self.root)
        
        
    def recHeight(self,root):
        if root == None:
            return 0
        
        leftH = self.recHeight(root.left)
        rightH = self.recHeight(root.right)
        
        if leftH>rightH:
            return 1+leftH
        else:
            return 1+rightH        
        
def main():
    avl = AVLTree()
    data = [3,1,9,6,0,11,2,5,4]
    
    for i in range(len(data)):
        avl.insert(data[i])
    
    avl.inOrderPrint()
    print("Height = ",avl.height())
    
if __name__ == "__main__":
    main()