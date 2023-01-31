class node:
    def __init__(self,data):
        self.data = data
        self.next = next


#stack인데 ?
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,data):
        newNode = node(data)
        if(self.head == None and self.tail == None):
            self.head = newNode
            self.tail = self.head 
        else:
            self.tail.next = newNode
            self.tail = newNode

    def delete(self):
        outNode = None
 

        

    def allPrint(self):
        node = self.head
        while(node.next!=None):
            print(node.data,end=" -> ")
            node = node.next
        
