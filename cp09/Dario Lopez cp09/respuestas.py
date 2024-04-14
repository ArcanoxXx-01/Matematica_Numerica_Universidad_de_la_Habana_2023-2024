import numpy as np

#Ejercicio 9

def F(x):
    return np.array([x[0]**2 + x[0]*x[1]**3 - 9])
def J(x):
    return np.array([[2*x[0] + x[1]**3, 3*x[0]*x[1]**2]])
def newton_method(F, J, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        Fx = F(x)
        if np.linalg.norm(Fx) < tol:
            print(f'Solución encontrada en la iteración {i+1}: x = {x}')
            return x
        Jx = J(x)
        h = np.linalg.solve(Jx, -Fx)
        x = x + h
    print("El método de Newton no converge después de", max_iter, "iteraciones.")
    return None
# Punto inicial
x0 = np.array([1.0, 1.0])
# Resolver el sistema de ecuaciones no lineales utilizando el método de Newton
newton_method(F, J, x0)

#Ejercicio 23 c)
def halley_method(f, df, d2f, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        d2fx = d2f(x)
        denominator = 2 * dfx**2 - fx * d2fx
        if denominator == 0:
            return None  #Hay division por 0
        x_new = x - 2 * fx * dfx / denominator
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return None  #No converge

# Ejemplo de uso:
def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

def d2f(x):
    return 6*x

Y = halley_method(f, df, d2f, 2)
print("Y:", Y)