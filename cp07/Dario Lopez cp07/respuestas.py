import autograd.numpy as np
from scipy.optimize import rosen, rosen_der
from autograd import grad, hessian

print()
print("====================Ejercicio 1========================")
print()
def f(x,y,z):
    return 3*x**2 + np.sin(y) * np.exp(x + z)

grad_f_x = grad(f)
hess_f_x = hessian(f)

print("Gradiente de f en x1:", grad_f_x(1.0,2.0,3.0))
print("Gradiente de f en x2:", grad_f_x(10.0,20.0,-3.0))
print("Hessiana de f en x1:", hess_f_x(1.0,2.0,3.0))
print("Hessiana de f en x2:", hess_f_x(10.0,20.0,-3.0))

print()
print("====================Ejercicio 2========================")
print()

def is_local_minimum(f, x_star):
    # Calcular el gradiente de f en el punto x*
    if f is grad : gradient = rosen_der
    else : gradient = grad(f)
    grad_at_x_star = gradient(x_star)
    
    # Comprobar si todas las derivadas parciales son cercanas a cero
    all_near_zero = np.all(np.isclose(grad_at_x_star, 0.0))
    
    return all_near_zero

print("==================  a)  ================================")
print()

def g(x):
    return (x[0]-2)**2 +(x[1]-3)**2

minimumx1 = is_local_minimum(g,np.array([2.0,3.0]))
minimumx2=is_local_minimum(g,np.array([2.0,2.0]))

if minimumx1:
    print("El punto (2,3) es un mínimo local de la función f.")
else:
    print("El punto (2,3) no es un mínimo local de la función f.")

if minimumx2:
    print("El punto (2,2) es un mínimo local de la función f.")
else:
    print("El punto (2,2) no es un mínimo local de la función f.")
print()
print("==================  b)  ================================")
print()
x=np.ones(10, dtype=float)

if is_local_minimum(rosen , x) :
    print("El punto (1,...,1) con 10 unos es un mínimo local de la función de Rosenbrock.")
else:
    print("El punto (1,...,1) con 10 unos no es un mínimo local de la función de Rosenbrock.")

xp=np.ones(1000,dtype=float)

if is_local_minimum(rosen , xp) :
    print("El punto (1,...,1) con 1000 unos es un mínimo local de la función de Rosenbrock.")
else:
    print("El punto (1,...,1) con 1000 unos no es un mínimo local de la función de Rosenbrock.")



