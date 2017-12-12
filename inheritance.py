class polygon:
    def __init__(self,n):
        self.no_of_sides=n
    def inputsides(self):
        self.sides=[input("enter side "+str(i+1)+" :") for i in range(self.no_of_sides)]
    def dispsides(self):
        print self.sides

class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
        #super().__init__(self,3)
        #self.no_of_sides=3

    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        tarea=(s*(s-a)*(s-b)*(s-c))  ** 0.5
        print'the area of triangle is %0.2f' %tarea


tri=triangle()
tri.inputsides()
tri.dispsides()
tri.area()
