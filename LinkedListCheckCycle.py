class Node:
    def __init__(self,value):
        self.value = value
        self.next = None  
        
def checkCycle(linklist):
    
    s = set()
    currentNode = linklist
    
    while(currentNode.next != None):
        #print("current: ", currentNode.value)
        if(currentNode.next in s):
            
                
            return 'There is cycle'
        else:
            s.add(linklist.next)
        currentNode = currentNode.next
            
    return 'There is no cycle'


a = Node(1)
b = Node(1)
c = Node(1)
d = Node(1)

a.next = b
b.next = c


print(checkCycle(a))

    