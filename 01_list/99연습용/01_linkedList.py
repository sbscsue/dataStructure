class node:
    def __init__(self,data):
        self.value = data
        self.next = None



class singleLinkedList:
    def __init__(self):
        self.head = None
    

    def size(self):
        check = self.head
        cnt = 0
        while(check!=None):
            cnt+=1
            check = check.next

        return cnt

    def search(self,value):
        check = self.head
        result = []

        i = 0
        while(check!=None):
            if(check.value==value):
                result.append(i)
            i += 1
            check = check.next

        return result
    
    def add(self,position,data):
        current = self.head
        prev = None
        i = 0

        n = node(data)
        
        while(current!=None):
            if(position==0):
                n.next = current
                self.head = current
                break
            if(i==position):
                prev.next = n
                n.next = current
                break

            prev = current
            current = current.next
            i+=1
        if(current==self.head):
            self.head = n
        else:
            prev.next = n


    #오류
    def remove(self,position):
        current = self.head
        prev = None
        i = 0

        while(current!=None and current!= self.head):
            if(position==0):
                n = current
                self.head = current.next
                return n.value
            if(i==position):
                n = current
                prev.next = current.next
                return n.value
            current = current.next
            i+=1
        if(current==self.head):
            self.head = n
        else:
            prev.next = n


    def peek(self,position):
        current = self.head
        prev = None
        i = 0

        while(current!=None):
            if(position==0):
                n = current
                return n.value
            elif(i==position):
                n = current
                return n.value
            current = current.next
            i+=1



            

            





ll = singleLinkedList()
ll.add(0,0)
ll.add(1,1)
ll.add(2,2)
ll.add(0,5)




print(ll.peek(0))
print(ll.peek(1))
print(ll.peek(2))
print(ll.peek(3))
print(ll.peek(4))

print(ll.remove(5))
print(ll.remove(4))
print(ll.remove(3))
print(ll.remove(2))
print(ll.remove(1))
print(ll.remove(0))

print("========================")
ll.add(0,0)
ll.add(1,1)
ll.add(2,2)
print(ll.peek(0))
print(ll.peek(1))
print(ll.peek(2))
print(ll.peek(3))
print(ll.peek(4))
print(ll.peek(5))


print("==========================")
ll.add(0,-1)
print(ll.peek(0))
print(ll.peek(1))
print(ll.peek(2))
print(ll.peek(3))
print(ll.peek(4))
print(ll.peek(5))


print("==========================")
ll.add(1,-2)
print(ll.peek(0))
print(ll.peek(1))
print(ll.peek(2))
print(ll.peek(3))
print(ll.peek(4))
print(ll.peek(5))




    
