class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def setData(self,newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

    def hasNext(self):
        return self.next != None

    def setPrev(self,prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        return self.prev != None

    def __str__(self):
        #return "Node[Data {0}]".format(self.data),
        return "Data[%d]" % self.data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.length += 1


    def insertAtEnd(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
            newNode.setPrev(current)
        self.length += 1


    def insertAtPos(self,data,index=0): # default position 0
        newNode = Node()
        newNode.setData(data)
        if self.head == None or index == 0:
            self.insertAtBeginning(data)
        elif index > 0:
            tempNode = self.getNode(index)
            if tempNode == None or tempNode.getNext() == None:
                self.insertAtEnd(data)
            else:
                preNode = tempNode.getPrev()
                if preNode != None:
                    newNode.setNext(tempNode)
                    tempNode.setPrev(newNode)
                    preNode.setNext(newNode)
                    newNode.setPrev(preNode)
                else:
                    self.insertAtBeginning(data)
                    self.length += 1
#--------------------------------------------------------------------------
#                 Delete a node

    def deleteAtBeginning(self):
        current = self.head
        nextNode = current.getNext()
        nextNode.setPrev(None)
        del current
        del self.head # free the memory
        self.head = nextNode
        self.length -= 1


    def deleteAtEnd(self):
        current = self.head
        while current.hasNext():
            current=current.getNext()
        preNode = current.getPrev()
        preNode.setNext(None)
        self.length -= 1


    def deleteAtPos(self,index=0):
        if index==0:
            self.deleteAtBeginning()
        elif index==self.length or index>self.length:
            self.deleteAtEnd()
        elif index<0:
            return
        else:
            currentNode = self.getNode(index)
            preNode=currentNode.getPrev()
            if preNode != None:
                nextNode = currentNode.getNext()
                preNode.setNext(nextNode)
                nextNode.setPrev(preNode)
                self.length -= 1
            else:
                self.deleteAtBeginning()

    def getNode(self,index):
        currentNode = self.head
        if currentNode == None:
            return None
        i=0
        while i < index-1:
            currentNode= currentNode.getNext()
            if currentNode == None:
                break
            i += 1
        return currentNode

    def traverse(self):
        current = self.head
        while current != None:
            print current.__str__(),
            current = current.getNext()

obj = DoubleLinkedList()
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.insertAtPos(6,5)
obj.traverse()
print
obj.deleteAtBeginning()
obj.traverse()
print
obj.deleteAtPos(-1)
#obj.deleteAtEnd()
obj.traverse()

print '\nLength :',obj.length
