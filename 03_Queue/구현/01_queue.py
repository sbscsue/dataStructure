class node:
    def node(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def Queue(self,data):
        self.head = node(data)
        self.tail = self.head

    def push(self,data):
        n = node(data)
        if(self.tail!=None):
            n.prev = self.tail
            self.tail.next = n

            self.tail = n
        else:
            self.head = n
            self.tail = self.head
        
    def peek(self):
        if(self.head!=None):
            print(self.head.data)
            
    def pop(self):
        if(self.head!=None):
            if(self.head!=self.tail):
                prev = self.tail.prev

                prev.next = None
                self.tail = prev

            else:
                self.head = None
                self.tail = None
            
        else:
            raise Exception('QueueEmpty') 
    
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
            


    