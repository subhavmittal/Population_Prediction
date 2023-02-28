import matplotlib.pyplot as plt
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
print()
print("Plotting the population of China and India and their difference.....")
# Plotting the population of China and India and their difference
iterator = 2000
x_array = []
y_array_China = []
y_array_India = []
y_array_diff = []
while iterator<=2026:
    x_array.append(iterator)
    iterator+=0.1
for i in x_array:
    China.evaluate(i)
    India.evaluate(i)
    y_array_China.append(China.get_polynomial())
    y_array_India.append(India.get_polynomial())
    y_array_diff.append(China.get_polynomial() - India.get_polynomial())
plt.plot(x_array,y_array_China,label="China")
plt.plot(x_array,y_array_India,label="India")
plt.plot(x_array,y_array_diff,label="Difference")
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Graph")
plt.plot(2000,1.28,'ro')
plt.annotate("(2000,1.28)",xy=(2000,1.28),xytext=(2000,1.28),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2005,1.31,'ro')
plt.annotate("(2005,1.31)",xy=(2005,1.31),xytext=(2005,1.31),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2010,1.35,'ro')
plt.annotate("(2010,1.35)",xy=(2010,1.35),xytext=(2010,1.35),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2015,1.39,'ro')
plt.annotate("(2015,1.39)",xy=(2015,1.39),xytext=(2015,1.39),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2023,1.41,'ro')
plt.annotate("(2023,1.41)",xy=(2023,1.41),xytext=(2023,1.41),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2000,1.04,'bo')
plt.annotate("(2000,1.04)",xy=(2000,1.04),xytext=(2000,1.04),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2005,1.1,'bo')
plt.annotate("(2005,1.1)",xy=(2005,1.1),xytext=(2005,1.1),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2010,1.2,'bo')
plt.annotate("(2010,1.2)",xy=(2010,1.2),xytext=(2010,1.2),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2015,1.32,'bo')
plt.annotate("(2015,1.32)",xy=(2015,1.32),xytext=(2015,1.32),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2023,1.40,'bo')
plt.annotate("(2023,1.40)",xy=(2023,1.40),xytext=(2023,1.40),ha = 'center',va = 'top',fontsize=8)
plt.plot(2000,0.24,'go')
plt.annotate("(2000,0.24)",xy=(2000,0.24),xytext=(2000,0.24),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2005,0.21,'go')
plt.annotate("(2005,0.21)",xy=(2005,0.21),xytext=(2005,0.21),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2010,0.15,'go')
plt.annotate("(2010,0.15)",xy=(2010,0.15),xytext=(2010,0.15),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2015,0.07,'go')
plt.annotate("(2015,0.07)",xy=(2015,0.07),xytext=(2015,0.07),ha = 'center',va = 'bottom',fontsize=8)
plt.plot(2023,0.01,'go')
plt.annotate("(2023,0.01)",xy=(2023,0.01),xytext=(2023,0.01),ha = 'center',va = 'bottom',fontsize=8)
plt.legend()    
plt.show()