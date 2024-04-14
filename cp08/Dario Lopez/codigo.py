
print("===============Pregunta 1 ================")
def f(x):
    # Define tu función f(x) aquí
    return x**2

# Método compuesto del rectángulo
def rectangulo_compuesto(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Método compuesto de los trapecios
def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Método compuesto del punto medio
def punto_medio_compuesto(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + (i + 0.5) * h)
    integral *= h
    return integral

# Método compuesto de Simpson
def simpson_compuesto(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par para el método de Simpson")
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        factor = 2 if i % 2 == 0 else 4
        integral += factor * f(a + i * h)
    integral *= h / 3
    return integral

# Ejemplo de uso
a = 0
b = 1
n = 1000  # Número de subintervalos
print("Resultado del método compuesto del rectángulo:", rectangulo_compuesto(f, a, b, n))
print("Resultado del método compuesto de los trapecios:", trapecio_compuesto(f, a, b, n))
print("Resultado del método compuesto del punto medio:", punto_medio_compuesto(f, a, b, n))
print("Resultado del método compuesto de Simpson:", simpson_compuesto(f, a, b, n))


print("===============Pregunta 4 ================")

import numpy as np
import matplotlib.pyplot as plt

def derivada_diferencias_finitas(f, x, h):
    return (f(x + h) - f(x)) / h

def graficar_funcion_y_derivada(f, a, b, h):
    x = np.linspace(a, b, 1000)
    y = f(x)
    derivada_aprox = derivada_diferencias_finitas(f, x, h)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.plot(x, derivada_aprox, label="f'(x) Aproximada (h={})".format(h))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Función y su derivada')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficar_error(f, x, h_values, valor_real):
    errores = []
    for h in h_values:
        derivada_aprox = derivada_diferencias_finitas(f, x, h)
        error = np.abs(derivada_aprox - valor_real)
        errores.append(error)

    plt.figure(figsize=(10, 6))
    plt.plot(h_values, errores, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Valor de h')
    plt.ylabel('Error')
    plt.title('Error de la aproximación de la derivada')
    plt.grid(True)
    plt.show()

# Ejemplo de uso:
def f(x):
    return np.sin(x)

a = 0
b = np.pi/2
x_bar = np.pi/4
h_values = np.logspace(-10, 0, 100)  # Valores de h desde 1e-10 hasta 1

# a) Valor de la derivada en x_bar
derivada_en_x_bar = derivada_diferencias_finitas(f, x_bar, 0.01)
print("Derivada de f(x_bar):", derivada_en_x_bar)

# b) Graficar la función y su derivada
graficar_funcion_y_derivada(f, a, b, 0.01)

# c) Graficar el error de la aproximación de la derivada para diferentes valores de h
valor_real = np.cos(x_bar)  # Derivada real de sin(x) es cos(x)
graficar_error(f, x_bar, h_values, valor_real)

print("===============Pregunta 6 ================")

def calcular_coeficientes_w(n):
    # Inicializar lista para almacenar los coeficientes w
    coeficientes_w = []

    # Calcular el ancho de cada segmento
    h = 1 / n

    # Calcular los coeficientes w
    coeficientes_w.append(h / 2)  # Primer coeficiente
    for i in range(1, n):
        coeficientes_w.append(h)  # Coeficientes intermedios
    coeficientes_w.append(h / 2)  # Último coeficiente

    return coeficientes_w

# Ejemplo de uso:
n = 4
coeficientes = calcular_coeficientes_w(n)
print("Los coeficientes w son:", coeficientes)

print("===============Pregunta 7 ================")

import sympy as sp

def calcular_derivada_aproximada(f, x, h, n, p):
    # Crear símbolo para h
    hh = sp.Symbol('h')
    
    # Crear puntos equiespaciados para la interpolación
    puntos = [(x + i * hh, f.subs(x + i * hh)) for i in range(-n, n+1)]
    
    # Calcular el polinomio de interpolación de Lagrange
    polinomio_interp = sp.interpolate(puntos, sp.symbols('x'))
    
    # Calcular la derivada n-ésima del polinomio de interpolación
    derivada_n = polinomio_interp.diff(x, n)
    
    # Evaluar la derivada en el punto x con h = 0
    derivada_aprox = derivada_n.subs(hh, h)
    
    # Calcular hbest
    hbest = (sp.factorial(n) * (h ** p)) ** (1 / (n + p))
    
    return derivada_aprox, hbest

# Ejemplo de uso:
x = sp.Symbol('x')
f = sp.sin(x)  # Función de ejemplo
n = 1  # Orden de la derivada
p = 2  # Orden del error deseado
x_valor = 0  # Punto donde se desea aproximar la derivada
h_valor = 0.1  # Valor de h
derivada_aprox, hbest = calcular_derivada_aproximada(f, x_valor, h_valor, n, p)

print("Aproximación de la derivada:", derivada_aprox)
print("Valor recomendado de h (hbest):", hbest)


print("===============Pregunta 8 ================")
def integral_interpolacion(f, a, b, n):
    # Definir símbolo x
    x = sp.Symbol('x')
    
    # Calcular los nodos de interpolación equidistantes
    nodos = [a + k*(b - a)/(n - 1) for k in range(n)]
    
    # Calcular los coeficientes del polinomio de interpolación
    polinomio = 0
    for k in range(n):
        L_k = 1
        for j in range(n):
            if j != k:
                L_k *= (x - nodos[j]) / (nodos[k] - nodos[j])
        polinomio += f(nodos[k]) * L_k
    
    # Calcular la integral del polinomio de interpolación en el intervalo [a, b]
    integral = sp.integrate(polinomio, (x, a, b))
    
    return integral

# Ejemplo de uso:
f = sp.sin(x)  # Función de ejemplo
a = 0  # Límite inferior del intervalo
b = sp.pi  # Límite superior del intervalo
n = 3  # Número de puntos de interpolación

integral = integral_interpolacion(f, a, b, n)
print("La integral aproximada es:", integral)