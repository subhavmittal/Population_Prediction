#Use secant method to find roots of a function
#Use bisection method to get initial guesses
import math
def f(x):
    return x**4 +x**3+5*x**2 - 3*x + 1
class FindRoot:
    def __init__(self,a,b,f,N0,tol=1e-5):
        self.a = a
        self.b = b
        self.f = f
        self.tol = tol
        self.maxiter = N0
    def bisection(self):
        FA = self.f(self.a)
        N0 = math.ceil(math.log(abs((self.b-self.a))/0.5, 2))
        for i in range(N0):
            c = self.a + (self.b-self.a)/2
            F = self.f(c)
            if FA*F < 0:
                self.b = c
            else:
                self.a = c
                FA = F
        print("Initial guesses are",self.a,"and",self.b)        
    def secant(self):
        self.bisection()
        q0 = self.f(self.a)
        q1 = self.f(self.b)
        p0 = self.a
        p1 = self.b
        numsteps = 0
        for i in range(self.maxiter):
            p = p1 - q1*(p1-p0)/(q1-q0)
            print("p = ",p) 
            numsteps += 1
            if abs(p-p1) < self.tol:
                print("Root is", p)
                print("Number of steps",numsteps)
                return
            p0 = p1
            p1 = p
            q0 = q1
            q1 = self.f(p)
        if(numsteps == self.maxiter):
            print("Method failed after",self.maxiter,"steps")
   
test = FindRoot(0,2,f,15,1e-9)
test.secant()