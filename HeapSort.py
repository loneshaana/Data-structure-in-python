class HeapSort:
    def __init__(self):
        self.heaplength = []
        self.size =0
        self.sorted=[]


    def sort(self,alist):
        #get the list do minheap to the list
        #create the min heap first
        self.minHeap(alist)
        while self.size >=0:
            self.delMin()
        return self.sorted


    def minHeap(self,alist):
        if len(alist) !=0:
            self.heaplist = [] +alist[:]
            self.size =len(self.heaplist) - 1
            index = self.size //2
            while index>-1:
                self.perculateDownForMinHeap(index)
                index -=1
            #return self.heaplist


    def perculateDownForMinHeap(self,index):
        if self.size >0:
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


    def delMin(self):
        if self.size >=1:
            self.sorted.append(self.heaplist[0])
        #    print 'sorted array :',self.sorted
            self.heaplist[0] =  self.heaplist[self.size]
            self.heaplist.pop()
            self.size -=1
        #    print 'Heap Array :',self.heaplist
        #    print 'Size of Heap :',self.size
            self.perculateDownForMinHeap(0)
            return self.heaplist
        elif (self.size == 0) and len(self.heaplist)==1:
            self.sorted.append(self.heaplist.pop())
            self.size -= 1
        else:
            return None


obj= HeapSort()
import timeit
start = timeit.default_timer()
obj.sort(range(1000000,0,-1))
stop = timeit.default_timer()
print 'Total time :',stop-start
