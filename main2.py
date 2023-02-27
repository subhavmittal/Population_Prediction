from background_functions import LagrangePolynomial,bisection,newton
#China population data    
x1 = [(2000,1.28),(2005,1.31),(2010,1.35),(2015,1.39),(2023,1.41)]
#India population data
x2 = [(2000,1.04),(2005,1.1),(2010,1.2),(2015,1.32),(2023,1.40)]
# Making a Lagrange Polynomial object for China    
China = LagrangePolynomial(5)
China.load_data(x1)    
China.generate_coefficients()
# Making a Lagrange Polynomial object for India
India = LagrangePolynomial(5)
India.load_data(x2)
India.generate_coefficients()
print("Loaded data for China and India")
print()
# Making a list of derivatives of China and India at the given points
# We only need 4 points since the derivative of a 4th order polynomial is a 3rd order polynomial
x_der1 = []
x_der2 = []
input = [2000,2005,2010,2015]
for i in input:
    China.evaluate(i)
    India.evaluate(i)
    x_der1.append((i,China.get_derivative()))
    x_der2.append((i,India.get_derivative()))
print("Made a list of derivatives of China and India at the given points")    
# Making a Lagrange Polynomial object for derivative of China and India population  
China_der = LagrangePolynomial(4)
India_der = LagrangePolynomial(4)
China_der.load_data(x_der1)
India_der.load_data(x_der2)
China_der.generate_coefficients()
India_der.generate_coefficients()
print("Loaded data for derivatives of China and India")
print()
#Finding an initial estimate of root of China_der and India_der using bisection method
print("Bisection Method")
bisection_tol = 0.5
intitial_root,numsteps_bisection = bisection(2000,2026,China_der,India_der,bisection_tol)
if intitial_root==-1:
    print("Let's take 2023 as the initial root estimate")
    intitial_root = 2023
else:    
    print("Initial root estimate:",intitial_root)
    print("Number of steps taken:",numsteps_bisection)
print()
# Finding the precise root using Newton's method
print("Newton's Method")
maxiter_newton = 10
newton_tol = 1e-9   
root_final,numsteps_newton = newton(intitial_root,China_der,India_der,maxiter_newton,newton_tol)
if root_final==-1:
    print("Method failed after",maxiter_newton,"steps")
else:
    print("Final Root:",root_final)
    print("Number of steps taken:",numsteps_newton)
print()
print("The difference between the populations at the extremum is:")    
China.evaluate(root_final)
India.evaluate(root_final)
print(China.get_polynomial()-India.get_polynomial())