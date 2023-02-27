# Generate Lagrange Interpolating Polynomials for China and India's population data using divided difference
# Find an initial estimate of root of the difference of the 2 polynomials using bisection method
# Find the precise root using Newton's method
# Use horner's method (modified for divided difference coefficients) to evaluate the polynomials and their derivatives
# We don't use neville's method to evaluate polynomials as it takes O(n^2) time 
# Whereas horner's method takes O(n) time


# Importing the required libraries
import matplotlib.pyplot as plt
import math
# Defining a class to generate Lagrange Interpolating Polynomials
class LagrangePolynomial:
    def __init__(self,n):
        # n is the number of data points
        self.n = n
        # Initializing the x and f(x) values
        self.x = [0 for i in range(n)]
        self.fx = [0 for i in range(n)]
        # Initializing the divided difference coefficients
        self.a = [0 for i in range(n)]
        # Initializing the value of the polynomial and its derivative at a point
        self.pol = 0
        self.der = 0
        
    # Loads the population data into the x and f(x) values    
    def load_data(self,x):
        for i in range(self.n):
            # Stores the years as the x values in reverse order
            self.x[self.n - 1 - i] = x[i][0]
            # Stores the population of the country in billions as the y values
            self.fx[i] = x[i][1]
    
    # Generates the divided difference coefficients       
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
            
    # Evaluates the polynomial and its derivative at a point y       
    def evaluate(self,y):
        # bn = an
        val= self.a[0]
        der = val
        for i in range(1,self.n-1):
            # bk = ak + (y - xk)*bk+1
            val = val*(y - self.x[i]) + self.a[i]
            der = der*(y - self.x[i+1]) + val
        # b0 = a0 + (y - x0)*b1    
        val = val*(y - self.x[self.n-1]) + self.a[self.n - 1]
        self.pol = val
        self.der = der
    def get_polynomial(self):
        return self.pol
    def get_derivative(self):
        return self.der

# function to find the root of the difference of the 2 polynomials using bisection method
def bisection(a,b,LagrangePolynomial1,LagrangePolynomial2,tol=1e-5):
    # finding f(a) stored in FA and f(b) stored in FB
    LagrangePolynomial1.evaluate(a)
    LagrangePolynomial2.evaluate(a)
    FA = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
    LagrangePolynomial1.evaluate(b)
    LagrangePolynomial2.evaluate(b)
    FB = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
    # Checking if the root is in the interval
    if FA*FB > 0:
        print("Function endpoints are of same sign")
        return -1,-1
    # Initializing the number of steps
    numsteps = 0
    # Finding the number of steps required to reach the desired tolerance
    N0 = math.ceil(math.log(abs((b-a))/tol,2))
    for i in range(N0):
        c = a + (b-a)/2
        # finding f(c) stored in F
        LagrangePolynomial1.evaluate(c)
        LagrangePolynomial2.evaluate(c)
        F = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
        # Incrementing the number of steps
        numsteps += 1
        # Checking if the root is found
        if F == 0:
            return c,numsteps
        # Checking if the root is in the left half
        elif FA*F < 0:
            b = c
        # Checking if the root is in the right half    
        else:
            a = c
            FA = F
    return c,numsteps

# function to find the root of the difference of the 2 polynomials using Newton's method        
def newton(p0,LagrangePolynomial1,LagrangePolynomial2,maxiter,tol=1e-5):
    # Initializing the number of steps
    i = 0
    while i<maxiter:
        # Evaluating the polynomials and their derivatives at p0
        LagrangePolynomial1.evaluate(p0)
        LagrangePolynomial2.evaluate(p0)
        # pol = f(p0) and der = f'(p0)
        pol = LagrangePolynomial1.get_polynomial() - LagrangePolynomial2.get_polynomial()
        der = LagrangePolynomial1.get_derivative() - LagrangePolynomial2.get_derivative()
        # Finding the next point p and checking if the derivative is 0
        try:
            p = p0 - pol/der
            print("p =",p)
        except:
            print("Division by zero")
        # Checking if the root is found within the desired tolerance     
        if(abs(p-p0) <= tol):
            return p,i+1
        # Updating the value of p0 and incrementing the number of steps
        p0 = p
        i += 1
        
    # If the root is not found within the desired tolerance, return -1,-1    
    return -1,-1
        