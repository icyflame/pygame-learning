class vector(object):

    def __init__(self,list1,list2):

        self.diff = (list2[0]-list1[0],list2[1]-list1[1])
        
        print self.diff


    def distance(self):

        a = self.diff[0]

        b = self.diff[1]

        self.a = a

        self.b = b

        import math

        return math.sqrt(a**2+b**2)


    def unit(self):

        hypotenuse = self.distance()

        self.aunit = self.a/hypotenuse

        self.bunit = self.b/hypotenuse

        return (self.aunit,self.bunit)


    def add(self,x,y):

        self.sum = (x[0]+y[0],x[1]+y[1])

        return self.sum


a = (20.0,25.0)

b = (50.0,65.0)

c = vector(a,b)

print c.distance()

print 'the sum is:',c.unit()

print c.add(a,b)
