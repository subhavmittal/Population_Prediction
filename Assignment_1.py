# Generate Lagrange Interpolating Polynomials for China and India's population data using divided difference
# Find root of the difference of the 2 polynomials using Newton's method
# Use horner's method to evaluate the polynomials and their derivatives
# We don't use neville's method to evaluate polynomials as it takes O(n^2) time 
# Whereas horner's method takes O(n) time
import matplotlib.pyplot as plt
class LagrangePolynomial:
    def __init__(self,n):
        self.n = n
        self.x = [0 for i in range(n)]
        self.fx1 = [0 for i in range(n)]
        self.fx2 = [0 for i in range(n)]
        self.a1 = [0 for i in range(n)]
        self.a2 = [0 for i in range(n)]
    def load_population_data(self,x1,x2):
        for i in range(self.n):
            # Stores the years as the x values
            self.x[self.n - 1 - i] = x1[i][0]
            # Stores the population of china in billions as the y values
            self.fx1[i] = x1[i][1]
            # Stores the population of india in billions as the y values
            self.fx2[i] = x2[i][1]
    def generate_polynomial(self):
        # Initializing the divided difference tables for both china and india
        F1 = [[0 for j in range(i+1)] for i in range(self.n)]
        F2 = [[0 for j in range(i+1)] for i in range(self.n)]
        # First column of the table is the f(x) values
        for i in range(self.n):
            F1[i][0] = self.fx1[i]
            F2[i][0] = self.fx2[i]
        # Generating the divided difference tables recursively    
        for i in range(1,self.n):
            for j in range(1,i+1):
                F1[i][j] = (F1[i][j-1] - F1[i-1][j-1])/(self.x[self.n - 1 - i] - self.x[self.n - 1 - (i-j)])
                F2[i][j] = (F2[i][j-1] - F2[i-1][j-1])/(self.x[self.n - 1 - i] - self.x[self.n - 1 - (i-j)])
        # Storing the coefficients of the polynomials ak [k = n-1 to 0]     
        for i in range(self.n):
            self.a1[self.n - 1 - i] = F1[i][i]
            self.a2[self.n - 1 - i] = F2[i][i]
    def evaluate_polynomial(self,y):
        val_1 = self.a1[0]
        der_1 = val_1
        val_2 = self.a2[0]
        der_2 = val_2
        for i in range(1,self.n-1):
            val_1 = val_1*(y - self.x[i]) + self.a1[i]
            der_1 = der_1*(y - self.x[i+1]) + val_1
            val_2 = val_2*(y - self.x[i]) + self.a2[i]
            der_2 = der_2*(y - self.x[i+1]) + val_2
        val_1 = val_1*(y - self.x[self.n-1]) + self.a1[self.n - 1]
        val_2 = val_2*(y - self.x[self.n-1]) + self.a2[self.n - 1]
        diff = val_1 - val_2
        der = der_1 - der_2    
        return val_1,val_2
    def bisection(self):
        pass
    def newton(self):
        pass
#China population data    
x1 = [(2000,1.28),(2005,1.31),(2010,1.35),(2015,1.39),(2023,1.41)]
#India population data
x2 = [(2000,1.04),(2005,1.1),(2010,1.2),(2015,1.32),(2023,1.40)]    
test = LagrangePolynomial(5)
test.load_population_data(x1,x2)    
test.generate_polynomial()

            