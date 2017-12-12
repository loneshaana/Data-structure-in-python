class Heap:
    def __init__(self):
        self.heaplist = [0]
        self.size =0
        self.minele = 'Call bulidMinHeap First'
        self.maxele = 'Call bulidMaxHeap First'

    def buildMaxHeap(self,hlist):
        self.heaplist = [] + hlist[:]
        self.size = len(self.heaplist) -1
        i = (self.size //2)
        while i >-1:
            self.perculateDownForMaxHeap(i)
            i=i-1
        self.maxele = self.heaplist[0]
        return self.heaplist

    def perculateDownForMaxHeap(self,index):
        while index*2 < self.size:
            maxIndex = self.getMax(index)
            if self.heaplist[maxIndex] > self.heaplist[index]:
                tmp = self.heaplist[index]
                self.heaplist[index] = self.heaplist[maxIndex]
                self.heaplist[maxIndex] = tmp
            index= maxIndex


    def getMax(self,i):
        # check its left and right child
        # return max child
        if i*2+2 > self.size:
            if i*2+1 <= self.size:
                return i*2+1
        elif self.heaplist[i*2+1] > self.heaplist[i*2+2]:
            return i*2+1
        else:
            return i*2+2

    def bulidMinHeap(self,hlist):
        if len(hlist) ==0:
            return
        self.heaplist = []+hlist[:]
        self.size = len(hlist)-1
        i = self.size //2
        while i > -1:
            self.perculateDownForMinHeap(i)
            i = i-1
        self.minele = self.heaplist[0]
        return self.heaplist


    def perculateDownForMinHeap(self,index,flag=''):
        while index*2 < self.size:
            minIndex = self.getMin(index)
            if self.heaplist[minIndex] < self.heaplist[index]:
                tmp = self.heaplist[index]
                self.heaplist[index] = self.heaplist[minIndex]
                self.heaplist[minIndex] = tmp
            index = minIndex

    def getMin(self,index):
        if index*2+2 > self.size:
            if index*2+1 <= self.size:
                return index*2+1
                pass
        elif self.heaplist[index*2+1] > self.heaplist[index*2+2]:
            return index*2+2 # returning minimum
        else:
            return index*2+1

    def traverse(self):
        if self.size ==0:
            return
        else:
            return self.heaplist

    def getParent(self,item):
        if self.size !=0:
            if item in self.heaplist:
                 index = self.heaplist.index(item)
                 if index ==0:
                     return '{} is the Root Element'.format(item)
                 if index %2 ==0:
                     #its parent is at(index-1) //2
                     index = (index-1)//2
                     return self.heaplist[index]
                 else:
                     #its parent is at index//2
                     index = index//2
                     return self.heaplist[index]
            else:
                return None
        else:
            return 'No Element In Heap Run Max heap of Min heap'

    def getChildrens(self,item):
        pass # here i is the parent node

    def delRoot(self):
        if self.size >1:
            first_ele = self.heaplist[0]
            self.heaplist[0] =  self.heaplist[self.size]
            self.heaplist.pop()
            self.size -=1
            self.perculateDownForMinHeap(0,flag='delroot')
            return self.heaplist

        elif self.size == 1:
            self.heaplist.pop()
        else:
            return None

    def maxInMinHeap(self):
        max= -1
        size = self.size + 1
        for i in range(size//2,size):
            if self.heaplist[i] > max:
                max =self.heaplist[i]
        return max

    def deleteNode(self,i):
        if i>self.size:
            print "Wrong Position"
            return
        key = self.heaplist[i]
        self.heaplist[i] = self.heaplist[self.size]
        self.size -=1
        self.perculateDownForMinHeap(i)
        return key


obj = Heap()
#print obj.buildMaxHeap([1,2,3,4,5,6,7,8,10,3,1])
print  obj.bulidMinHeap([121,33,11,10,9,8,7,6,5,4,3,2,1])
#print 'max Element :',obj.maxele
#print 'min Element :',obj.minele
#print 'Get Parent :',obj.getParent(1)
#print 'after deleting root heap is'
#print obj.delRoot()
#print obj.maxInMinHeap()
print obj.deleteNode(4)
print obj.traverse()
