# DATA STRUDTURE\Thinking\
# BST - Binary Search Tree

# Node of a Binary Search Tree
class BST(object):
    #constructor
    def __init__(self,data,left=None,right=None):
        self.data = data
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

    
#Search the key from node, iteratively
def find(root, data):
    current = root
    
    while(current is not None and data!=current.getData()):
        if data>current.getData():
            current = current.getright()
        else:
            current = current.getLeft()
    
    return current

#Search the key from node, recursively
def findRec(root,data):
    current = root
    if data == current.getData():
        return current
    if data < current.getData():
        findRec(current.getLeft, data)
    elif data > current.getData():
        findRec(current.getRight, data)
    else:
        return None

def findMin(root):
    current = root
    if current.getLeft() == None:
        return currentNode
    else:
        return findMin(current.getLeft())

def findMin(root, parent):
    """return the minimum node in the current tree and its parent"""
    #we use an ugly trick: the parent node is passed in as an argument
    #so that eventually when the leftmost child is reached , the call
    #can return both the parent to the successor and the successor 
    if root.left:
        return findMin(root.left, root)
    else:
        return [parent, root]
    
def findMax(root):
    current = root 
    if current.getright() == None:
        return current
    else:
        return findMax(current.getRight())

def successorBST(root):
    temp = None
    if root.getRight():
        temp = root.getRight()
        
        while temp.getLeft() :
            temp = temp.getLeft()
            
    return temp

def predecessorBST(root):
    temp = None
    if root.getLeft():
        temp = root.getLeft()
        
        while temp.getRight():
            temp = temp.getRight()
            
    return temp
    
def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def deleteNode(root,data):
    '''delete the node with the given data and return the root node of the tree'''
    if root.data == data:
        # found the node we need to delete
        if root.right and root.left:
            # get the successor node and its parent
            [psucc, succ] = findMin(root.right,root)
            # splice out the successor
            # we need the parent to do this
            if psucc.left == succ:
                psucc.left = succ.right
            else:
                psucc.right = succ.right
            # reset the left and right children of the successor
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            # "easier" case
            if root.left:
                return root.left    # promote the left subtree
            else:
                return root.right   # promote the right subtree
    else:
        if root.data > data:    # data should be in the left subtree
            if root.left:
                root.left = deleteNode(root.left, data)               
        else:   # else the data is not in the tree
            if root.right:  
                root.right = deleteNode(root.right, data)
    return root

#Height of the tree
def height(root):
    if root == None:
        return 0
    
    leftH = height(root.left)
    rightH = height(root.right)
    if leftH>rightH:
        return 1+leftH
    else:
        return 1+rightH

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.getData(),end=' ')
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.getData(),end=' ')
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    if not root:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.getData(),end=' ')

def main():
    print('\t\t\tBinary Search Tree')
    root = BST(35) 
    insertNode(root, BST(15))
    insertNode(root, BST(6))
    insertNode(root, BST(78))
    insertNode(root, BST(85))
    insertNode(root, BST(9))
    insertNode(root, BST(46))
    insertNode(root, BST(37))
    insertNode(root, BST(26))
    insertNode(root, BST(1))
    deleteNode(root, 26)
    inorder(root)
    print('')
    preorder(root)
    print('')
    postorder(root)
    print('')
    print("The Height of Tree is : ",height(root))
if __name__ == '__main__':
    main()
            
