class Queue:
    def __init__(self, limit=1):
        self.que = []
        self.rear = -1
        self.front = -1
        self.size = 0
        self.limit = limit

    def getSize(self):
        return self.size

    def enQueue(self,item):
        if len(self.que) >= self.limit:
            print 'Queue OverFlow'
            return 0
        else:
            self.que.append(item)
            self.size += 1
            print 'enQueue :',[item.data for item in self.que]
            print 'Total size of que',len(self.que)
            if self.front == -1:
                self.front = self.rear=0
                #self.size +=1
            else:
                #self.size += 1
                self.rear = self.getSize()

    def deQueue(self):
        if self.getSize() <= 0:
            print "Queue UnderFlow"
            return 0
        else:
            dequed = self.que.pop(0)
            self.size -= 1
            if self.getSize() == 0 :
                self.front = self.rear = 0
            else:
                self.rear = self.getSize() -1
            return dequed

    def queueRear(self):
        if self.isEmpty():
            if self.rear == -1:
                print "Queure Is Empty:"
            return ""
        return self.que[-1]

    def queueFront(self):
        if self.isEmpty():
            if self.front == -1:
                print "Queue Is Empty:"
            return ""
        return self.que[0]

    def length(self):
        return self.size

    def isEmpty(self):
        if self.getSize() <= 0:
            return True
        return False
if __name__ =="__main__":
    que = Queue()
    que.enQueue('first')
    print 'Size :',que.getSize()
    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
    que.enQueue('second')
    print 'Size :',que.getSize()

    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
    que.enQueue('third')
    print 'Size :',que.getSize()

    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
    print '-------------------------------'
    que.deQueue()
    print 'Size :',que.getSize()

    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
    que.deQueue()
    print 'Size :',que.getSize()

    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
    que.deQueue()
    print 'Size :',que.getSize()

    print "Front :"+que.queueFront()
    print "Rear :"+que.queueRear()
