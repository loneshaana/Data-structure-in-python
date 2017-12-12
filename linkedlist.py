#PROTOTYPE OF NODE
class Node:
    def __init__(self):
        self.data = None
        self.next = None

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


class LinkedList:
    def __init__(self,head = None):
        self.head = head
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def listLength(self ):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        self.length = count
        return count
#_______________________________________________________________________________
#              INSERTION IN LINKED LIST
    def __insertAtEnd__(self,data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(newNode)
        self.length +=1

    def __insertAtBeginning__(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.listLength == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1

    def insertAtPos(self,data,pos=0):
        if pos < 0:
            return None
        else:
            if pos == 0 or pos == 1:
                self.__insertAtBeginning__(data)
            else:
                if pos == self.length or pos > self.length:
                    self.__insertAtEnd__(data)
                else:
                    current = self.head
                    count = 0
                    while count < pos-1:
                        current = current.getNext()
                        count += 1
                    newNode = Node()
                    newNode.setData(data)
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    #increase the length
                    self.length += 1
#_______________________________________________________________________________
                        # DELETION IN A LIST

    def __deleteAtBeginning__(self):
        current = self.head
        del self.head   # optional remove memory
        self.head = current.getNext()
        self.length -= 1


    def __deleteAtEnd__(self):
        current = self.head
        previous = self.head
        while current.hasNext():
            previous = current
            current = current.getNext()

        del current
        previous.setNext(None)
        self.length -= 1


    def deleteAtPos(self,pos=0):  # default position 0
        if pos > self.length or pos < 0:
            raise IndexError("Index Error")
        else:
            if pos == 0 or pos == 1:
                self.__deleteAtBeginning__()
            else:
                if pos == self.length:
                    self.__deleteAtEnd__()
                else:
                    current = self.head
                    count = 0
                    previous = self.head
                    while count < pos-1:
                        count += 1
                        previous = current
                        current = current.getNext()
                    previous.setNext(current.getNext())
                    self.length -= 1


    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found


    def traverse(self):
        current = self.head
        while current != None:
            print(current.data),
            current = current.getNext()


obj = LinkedList()
obj1 = LinkedList()

obj.insertAtPos(1)
obj1.insertAtPos(11)

obj.insertAtPos(2,2)
obj1.insertAtPos(123,2)

obj.insertAtPos(3,3)
obj.insertAtPos(0)
obj.traverse()
print
obj.deleteAtPos(4)
print'--------------------------'
obj.traverse()
print'--------------------------'
obj1.traverse()
print('Length : ',obj.listLength())
