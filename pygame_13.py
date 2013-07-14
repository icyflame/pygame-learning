##beginning vectors


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


a = (20.0,25.0)

b = (50.0,65.0)

c = vector(a,b)

print c.distance()
