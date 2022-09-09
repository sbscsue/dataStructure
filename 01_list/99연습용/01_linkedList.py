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
        while(check.next!=None):
            cnt+=1
            check = check.next

        return cnt

    def search(self,value):
        check = self.head
        result = []
        i = -1
        while(check.next!=None):
            if(check.value==value):
                result.append(i)
            i += 1
            check = check.next
        return result
    
    def add(self,position,data):
        current = self.head
        i = -1
        while(current.next!=None):
            if(i == (position-1)):
                tmp = current.next 
                current.next = node(data)
                current.next.next = tmp
                break
        current.next = node(data)
    
    def remove(self,position):
        current = self.head
        i = -1
        while(current.next!=None):
            if(i == (position-1)):
                if(current.next.next!=None):
                    current.next = current.next.next
                else:
                    current.next = None
                break


ll = singleLinkedList()
ll.add(0,1)
    
