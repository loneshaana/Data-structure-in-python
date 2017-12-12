class stack:
    def __init__(self,limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <=0

    def push(self,item):
        if len(self.stk) >= self.limit:
            print "stack overflow"
        else:
            self.stk.append(item)
            #print 'stack after push :',self.stk

    def pop():
        if len(self.stk) <=0:
            print "stack underflow"
        else:
            return self.stk.pop()

    def peek(self):
        if len(stk) <=0:
            print "stack underflow"
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

if __name__ == "__main__":
    s = stack(100000000)
    map(s.push,range(100000000)) #pushing 1000 items
