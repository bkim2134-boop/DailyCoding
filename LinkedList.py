

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
            temp_1 = self.head
            while(temp_1.node_next != None):
                temp_1 = temp_1.node_next
            temp_1.node_next = temp    
                #iterate till end and then append
    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.node_next        

LL1 = LinkedList()        
LL1.add_node(10)
LL1.add_node(12)
LL1.add_node(5)

LL1.printList()
#going to use node for tree as well
#this is to ge faster and familiarize myself