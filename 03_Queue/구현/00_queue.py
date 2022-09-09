class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def push(self,data):
        n = node(data)
        if(self.isEmpty()):
           self.head = n
           self.tail = n 
        else:
            self.tail.next = n 
            self.tail = n 

            
    def pop(self):
        if(self.isEmpty()):
            pass
        else:
            if(self.head == self.tail):
                n = self.head
                self.head = None
                self.tail = None
                return n.data
            else:
                n = self.head
                self.head = self.head.next
                return (n.data)
            
    
    
    def isEmpty(self):
        if(self.head == None and self.tail == None):
            return True
        else:
            return False
            
q = Queue()
print(q.pop())
print("=================")
q.push(10)
q.push(20)
q.push(30)
q.push(40)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print("=================")
q.push(10)
print(q.pop())
print(q.pop())





    