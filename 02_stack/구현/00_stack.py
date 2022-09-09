from inspect import ismemberdescriptor


class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    
    def push(self,data):
        n = node(data)
        n.next = self.head
        self.head = n

    def pop(self):
        if(not self.isEmpty()):
            n = self.head
            self.head = n.next
            return n.data

    
    def peek(self):
        if(not self.isEmpty()):
            n = self.head 
            return n.data

s = stack()
print(s.pop())
print("=================")
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print("=================")
s.push(20)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
