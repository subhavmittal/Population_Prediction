# Generate Lagrange Interpolating Polynomials for China and India's population data using divided difference
# Find root of the difference of the 2 polynomials using Newton's method
# Use horner's method to evaluate the polynomials and their derivatives
# We don't use neville's method to evaluate polynomials as it takes O(n^2) time 
# Whereas horner's method takes O(n) time
import matplotlib.pyplot as plt
import math
class LagrangePolynomial:
    def __init__(self,n):
        self.n = n
        self.x = [0 for i in range(n)]
        self.fx = [0 for i in range(n)]
        self.a = [0 for i in range(n)]
        self.pol = 0
        self.der = 0
    def load_data(self,x):
        for i in range(self.n):
            # Stores the years as the x values
            self.x[self.n - 1 - i] = x[i][0]
            # Stores the population of the country in billions as the y values
            self.fx[i] = x[i][1]
    def generate_coefficients(self):
        # Initializing the divided difference tables for both china and india
        F = [[0 for j in range(i+1)] for i in range(self.n)]
        # First column of the table is the f(x) values
        for i in range(self.n):
            F[i][0] = self.fx[i]
        # Generating the divided difference tables recursively    
        for i in range(1,self.n):
            for j in range(1,i+1):
                F[i][j] = (F[i][j-1] - F[i-1][j-1])/(self.x[self.n - 1 - i] - self.x[self.n - 1 - (i-j)])
        # Storing the coefficients of the polynomials ak [k = n-1 to 0]     
        for i in range(self.n):
            self.a[self.n - 1 - i] = F[i][i]
    def evaluate(self,y):
        val= self.a[0]
        der = val
        for i in range(1,self.n-1):
            val = val*(y - self.x[i]) + self.a[i]
            der = der*(y - self.x[i+1]) + val
        val = val*(y - self.x[self.n-1]) + self.a[self.n - 1]
        self.pol = val
        self.der = der
    def get_polynomial(self):
        return self.pol
    def get_derivative(self):
        return self.der

def bisection(a,b,LagrangePolynomial1,LagrangePolynomial2,tol=1e-5):
    LagrangePolynomial1.evaluate(a)
    LagrangePolynomial2.evaluate(a)
    FA = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
    numsteps = 0
    N0 = math.ceil(math.log(abs((b-a))/tol,2))
    for i in range(N0):
        c = a + (b-a)/2
        LagrangePolynomial1.evaluate(c)
        LagrangePolynomial2.evaluate(c)
        F = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
        numsteps += 1
        if F == 0:
            return c,numsteps
        elif FA*F < 0:
            b = c
        else:
            a = c
            FA = F
    return c,numsteps        
def newton(p0,LagrangePolynomial1,LagrangePolynomial2,maxiter,tol=1e-5):
    i = 0
    while i<maxiter:
        LagrangePolynomial1.evaluate(p0)
        LagrangePolynomial2.evaluate(p0)
        pol = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
        der = LagrangePolynomial1.get_derivative() - LagrangePolynomial2.get_derivative()
        try:
            p = p0 - pol/der
        except:
            print("Division by zero") 
        if(abs(p-p0) <= tol):
            return p,i+1
        p0 = p
        i += 1
    if(i == maxiter):
        return -1,-1    