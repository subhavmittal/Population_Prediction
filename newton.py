#Using newton's method to find roots of a function
#Use Horner's method to evaluate polynomials and their derivatives
#Use bisection method to get initial guesses

#You can compare the results of this program with the results of secant.py
#Newton's method converges faster than secant's method
#The number of steps required by newton's method = 4 in this case whereas
#The number of steps required by secant's method = 6 in this case
import math
class FindRoot:
    def __init__(self,n,A,a,b,N0,tol = 1e-5):
        self.n = n
        self.A = A
        self.a = a
        self.b = b
        self.tol = tol
        self.B_pol = 0
        self.B_der = 0
        self.maxiter = N0
    def horner(self,x):
        self.B_pol = self.A[0]
        self.B_der = self.B_pol
        for j in range(1,self.n):
            self.B_pol = self.B_pol*x + self.A[j]
            self.B_der = self.B_der*x + self.B_pol
        self.B_pol = self.B_pol*x + self.A[self.n]
    def bisection(self):
        self.horner(self.a)
        FA = self.B_pol
        N0 = math.ceil(math.log(abs((self.b-self.a))/0.5, 2))
        for i in range(N0):
            c = self.a + (self.b-self.a)/2
            self.horner(c)
            F = self.B_pol
            if FA*F < 0:
                self.b = c
            else:
                self.a = c
                FA = F
        print("Initial guess is",c)
        return(c)
    def newton(self):
        p0 = self.bisection()
        i = 0
        while i<self.maxiter:
            self.horner(p0)
            try:
                p = p0 - self.B_pol/self.B_der
                print("p = ",p)
            except:
                print("Division by zero") 
            if(abs(p-p0) < self.tol):
                print("Root is",p)
                print("Number of steps",i+1)
                return
            p0 = p
            i += 1
        if(i == self.maxiter):
            print("Method failed after",self.maxiter,"steps")

test = FindRoot(3,[1,5,-3,1],0,2,9,1e-9)
test.horner(1)                                
print("B_pol = ",test.B_pol)
print("B_der = ",test.B_der)
          
            
            
        
        