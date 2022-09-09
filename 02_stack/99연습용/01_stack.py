class node:
    def __init__(self,data):
        self.data = data
        self.next = None    


class stack:
    def __init__(self):
        self.head = None

    def __init__(self,data):
        self.head = node(data)

    def push(self,data):
        n = node(data)
        n.next = self.head
        self.head = n
        
    def peek(self):
        if(not self.isEmpty()):
            return self.head.data
        else:
            print("stack Empty")

    def pop(self):
        if(not self.isEmpty()):
            n = self.head
            self.head = self.head.next
            return n.data
        else:
            print("stack Empty")


    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False


s = stack(20)
s.push(30)
s.push(40)
s.push(50)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

s.push(20)
print(s.peek())
print(s.pop())
print(s.peek())
