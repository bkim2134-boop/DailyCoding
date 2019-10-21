

class LinkedList:
    head = None
    
    class Node:
        data = 0 
        node_next = None
        

        def __init__(self, data):
            self.data = data
            pass
            
    def __init__(self):

        self.head = None
    
    def add_node(self, data):
        temp = self.Node(data)
        if(self.head == None):
            self.head = temp
        else:
            #iterate till end and then append
            return

LL1 = LinkedList()        
LL1.add_node(10)
#going to use node for tree as well
#this is to ge faster and familiarize myself