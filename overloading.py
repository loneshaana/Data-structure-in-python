#operator overloading
class point(object):  # inherits the object class
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self): # gets called when ever we try to print object
        return '({0},{1})'.format(self.x,self.y)

    def __add__(a,b): # gets called when ever we try to add the two objects
        x=a.x + b.x
        y=a.y + b.y
        return point(x,y)

    def __sub__(a,b): # gets called when ever we try to add the two objects
        x=a.x - b.x
        y=a.y - b.y
        return point(x,y)
p1=point(1,2)
p2=point(3,4)
#print p1
print p1+p2  # since we are adding it ,it will call the special function __add__ function
# or we can do this print p1.__add__(p2) same as p1+p2
print p1-p2
