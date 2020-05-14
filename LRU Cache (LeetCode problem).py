class Node():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.previous=None


class LinkedList(object):
    def __init__(self):
        self.start=Node(None,None)
        self.end=Node(None,None)
        self.start.next=self.end
        self.end.previous=self.start
    def addAtBeginning(self,n):
        n.next=self.start.next
        n.previous=self.start
        n.next.previous=n
        self.start.next=n
    def deleteFromEnd(self):
        x=self.end.previous
        x.previous.next=self.end
        x.next.previous=x.previous
        x.next=None
        x.previous=None
        return x.key
    def moveToFront(self,n):
        n.previous.next=n.next
        n.next.previous=n.previous
        n.next=None
        n.previous=None
        self.addAtBeginning(n)
        
class LRU(LinkedList):
    def __init__(self,capacity):
        self.capacity=capacity
        self.x={}
        super(LRU,self).__init__()
    def get(self,key):
        if key in self.x:
            self.moveToFront(self.x[key])
            return self.x[key].value
        return -1
    def put(self,key,value):
        if key in self.x:
            self.x[key].value=value
            self.moveToFront(self.x[key])
        else:
            self.x[key]=Node(key,value)
            self.addAtBeginning(self.x[key])
        if len(self.x)>self.capacity:
            r=self.deleteFromEnd()
            self.x.pop(r)

cache=LRU(2)
cache.put(5,7)
cache.put(8,20)
print(cache.get(5))
cache.put(3,6)
print(cache.get(8))
cache.put(4,12)
print(cache.get(5))
print(cache.get(3))
print(cache.get(4))


