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
#Finding an initial estimate of root of the difference of the 2 polynomials using bisection method
#If the root exists, it is safely between 2000 and 2026
print("Bisection Method")
bisection_tol = 0.5
intitial_root,numsteps_bisection = bisection(2000,2026,China,India,bisection_tol)
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
newton_tol = 1e-3
root_final,numsteps_newton = newton(intitial_root,China,India,maxiter_newton,newton_tol)
if root_final==-1:
    print("Method failed after",maxiter_newton,"steps")
else:
    print("Final Root:",root_final)
    print("Number of steps taken:",numsteps_newton)

    
    
    