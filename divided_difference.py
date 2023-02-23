class div_diff:
    def __init__(self,n,x,fx1):
        self.n = n
        self.x = x
        self.fx1 = fx1
        self.a = [0 for i in range(n)]
    def gen_coeff(self):
        # Initializing the divided difference tables for both china and india
        F1 = [[0 for j in range(i+1)] for i in range(self.n)]
        # First column of the table is the f(x) values
        for i in range(self.n):
            F1[i][0] = self.fx1[i]
        # Generating the divided difference tables recursively    
        for i in range(1,self.n):
            for j in range(1,i+1):
                F1[i][j] = (F1[i][j-1] - F1[i-1][j-1])/(self.x[self.n - 1 - i] - self.x[self.n - 1 - (i-j)])
        # Storing the coefficients of the polynomials ak [k = n-1 to 0]     
        for i in range(self.n):
            self.a[self.n - 1 - i] = F1[i][i]
    def evaluate(self,x):
        p = self.a[0]
        p_der = p
        for i in range(1,self.n-1):
            p = p*(x - self.x[i]) + self.a[i]
            p_der = p_der*(x - self.x[i+1]) + p
        p = p*(x - self.x[self.n-1]) + self.a[self.n-1]    
        return(p,p_der)
test = div_diff(3,[3,2,1],[1,4,9])
test.gen_coeff()
print(test.evaluate(1.8))
            
        