import math
class FindRoot:
    def __init__(self,a,b,f,tol=1e-5):
        self.a = a
        self.b = b
        self.f = f
        self.tol = tol
    def bisection(self):
        FA = self.f(self.a)
        numsteps = 0
        N0 = math.ceil(math.log((self.b-self.a)/self.tol, 2))
        for i in range(N0):
            c = self.a + (self.b-self.a)/2
            F = self.f(c)
            numsteps += 1
            if F == 0:
                print("Root is", c)
                print("Number of steps",numsteps)
                return
            elif FA*F < 0:
                self.b = c
            else:
                self.a = c
                FA = F
        print("Root is", c)
        print("Number of steps",numsteps)
