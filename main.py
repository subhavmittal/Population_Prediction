from background_functions import LagrangePolynomial,bisection,newton
#China population data    
x1 = [(2000,1.28),(2005,1.31),(2010,1.35),(2015,1.39),(2023,1.41)]
#India population data
x2 = [(2000,1.04),(2005,1.1),(2010,1.2),(2015,1.32),(2023,1.40)]    
China = LagrangePolynomial(5)
China.load_data(x1)    
China.generate_coefficients()
India = LagrangePolynomial(5)
India.load_data(x2)
India.generate_coefficients()
root,numsteps = bisection(2000,2024,China,India,0.5)
root2,numsteps2 = newton(root,China,India,10,0.5)
if root2==-1:
    print("Method failed after",10,"steps")
    print("Lets find the minima of the difference of the 2 polynomials")
    print("We have to find the root of the derivative of the difference of the 2 polynomials")
# x_der = []
# x_der.append((2000,test.get_derivative(2000)))
# x_der.append((2005,test.get_derivative(2005)))
# x_der.append((2010,test.get_derivative(2010)))
# x_der.append((2015,test.get_derivative(2015)))
# x_dummy = [(2000,0),(2005,0),(2010,0),(2015,0)]
# check = LagrangePolynomial(4)
# check.load_data(x_der,x_dummy)
# check.generate_coefficients()
# root,numsteps = bisection(2000,2030,check.get_polynomial,0.5)
# root2,numsteps2 = newton(root,check.get_polynomial,check.get_derivative,10,1e-9)
# print(root2)
# print(test.get_polynomial(root2))




    
    
    