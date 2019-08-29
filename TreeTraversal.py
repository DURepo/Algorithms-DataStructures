class BinaryTree:
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild= None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        
        if(self.leftChild == None):
            t = BinaryTree(newNode)
            self.leftChild = t
            
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild 
            self.leftChild = t
    
    def insertRight(self, newNode):
        
        t = BinaryTree(newNode)
        if(self.rightChild == None):            
            self.rightChild = t
        else:
            t.rightChild = self.rightChild
            self.rightChild =t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key
            
        

               
def PreOrder(tree):
    
    if(tree != None):
        print(tree.getRootVal())
        PreOrder(tree.leftChild)
        PreOrder(tree.rightChild)

def InOrder(tree):
    if(tree!= None):
        InOrder(tree.leftChild)
        print(tree.getRootVal())
        InOrder(tree.rightChild)

def PostOrder(tree):
    
    if(tree!=None):
        PostOrder(tree.leftChild)
        PostOrder(tree.rightChild)
        print(tree.getRootVal())
    
    
r = BinaryTree('a')
r.insertLeft('b')
r.insertLeft('d')
r.insertRight('c')

PreOrder(r)
#InOrder(r)
#PostOrder(r)