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
x_der1 = []
x_der2 = []
input = [2000,2005,2010,2015]
for i in input:
    China.evaluate(i)
    India.evaluate(i)
    x_der1.append((i,China.get_derivative()))
    x_der2.append((i,India.get_derivative()))
China_der = LagrangePolynomial(4)
India_der = LagrangePolynomial(4)
China_der.load_data(x_der1)
India_der.load_data(x_der2)
China_der.generate_coefficients()
India_der.generate_coefficients()
root,numsteps = bisection(2000,2022,China_der,India_der,0.5)
print(root)
root2,numsteps2 = newton(root,China_der,India_der,10,1e-9)
print(root2)
print(numsteps2)
China.evaluate(root2)
India.evaluate(root2)
print(China.get_polynomial()-India.get_polynomial())




    
    
    