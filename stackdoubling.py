class stack:
    def __init__(self,limit=10):
        self.stk = limit*[None]
        self.limit = limit
        self.index = 0

    def isEmpty(self):
        return self.stk <=0

    def push(self,item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print 'stack after push :',self.stk
        self.index += 1

    def pop():
        if len(self.stk) <=0:
            print "stack underflow"
        else:
            self.stk.pop()

    def peek(self):
        if len(stk) <=0:
            print "stack underflow"
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        newstk = list(self.stk)
        length = len(self.stk)
        self.limit = 2*self.limit
        self.stk = newstk
        #for i in range(self.limit-length):
        #    self.stk.append(None)

s = stack(1)
map(s.push,range(100)) #pushing 1000 items
