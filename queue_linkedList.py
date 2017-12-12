class Node:
    def __init__(self,data =None,next =None):
        self.data = data
        self.next = None
        self.last = None

    def getData(self):
        return self.data
    def setData(self,newData):
        self.data = newData
    def setNext(self,newNext):
        self.next=newNext
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next !=None
    def setLast(self,newLast):
        self.last = newLast
    def getLast(self):
        return self.last

class Queue:
    def __init__(self):
        self.head =None
        self.size =0
        self.last =None

    def enQueue(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
            self.last = newNode
        else:
            current = self.head
            lastNode =self.last
            lastNode.setNext(newNode)
            self.last = newNode
        #print 'Enquied :',newNode.getData()
        self.size +=1

    def deQueue(self,optional=None):
        current = self.head
        if self.head is None:
            print "Queue Is Empty"
            return
        elif current.hasNext():
            self.head = current.getNext()
            #print 'Dequed :',current.getData()

        else:
            print 'Dequeing...'
            self.head = None
            self.traverse()
        self.size -=1

    def traverse(self):
        if self.head is not None:
            current = self.head
            while(current.hasNext()):
                print current.getData(),
                current = current.getNext()
            print current.getData()
        else:
            print "Queue Is Empty"

que = Queue()
map(que.enQueue,range(1000000)) # enque from 1 -50
print('Length:',que.size)
#que.traverse()
que.deQueue()
map(que.deQueue,range(10))  # deque first 10
#que.traverse()
print('Length:',que.size)
