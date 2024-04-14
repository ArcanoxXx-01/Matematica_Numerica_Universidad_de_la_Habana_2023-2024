import numpy as np
print("==========Respuestas pregunta 2==========")
# Datos de la tabla
x_values = np.array([1, 2, 3, 4])
f_values = np.array([2, 1, 6, 47])

# Coeficientes de los polinomios
coeff_p = [5, -27, 45, -21]
coeff_q = [1, -5, 8, -5, 3]

# Evaluación de los polinomios en los puntos dados
p_result = np.polyval(coeff_p, x_values)
q_result = np.polyval(coeff_q, x_values)

# Verificación de la condición de interpolación
print(p_result)
if np.allclose(p_result, f_values):
    print("El polinomio p(x) satisface la condición de interpolación.")
else:
    print("El polinomio p(x) no satisface la condición de interpolación.")

print(q_result)
if np.allclose(q_result, f_values):
    print("El polinomio q(x) satisface la condición de interpolación.")
else:
    print("El polinomio q(x) no satisface la condición de interpolación.")

print("==========Respuestas pregunta 5==========")
def Pol_Interpolacion(x_values, y_values):
    # Calcular los coeficientes del polinomio de interpolación
    coefficients = np.polyfit(x_values, y_values, len(x_values) - 1)
    
    return coefficients

x_values = [1, 2, 3, 4]
y_values = [2, 1, 6, 47]

coeficientes = Pol_Interpolacion(x_values, y_values)
print("Coeficientes del polinomio de interpolación:", coeficientes)        

print("==========Respuestas pregunta 7==========")
def divided_differences(points):
    n = len(points)
    F = [[0] * n for _ in range(n)]
    
    for i in range(n):
        F[i][0] = points[i][1]
    
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (points[i+j][0] - points[i][0])
    
    return [F[0][j] for j in range(n)]  


def newton_interpolation(points):
    n = len(points)
    differences = divided_differences(points)
    polynomial = f"{differences[0]}"
    for i in range(1, n):
        term = f"{differences[i]}"
        for j in range(i):
            term += f" * (x - {points[j][0]})"
        polynomial += f" + {term}"
    return polynomial

print("==========Respuestas pregunta 6==========")
def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    coefficients = [0] * n

    for i in range(n):
        numerator = []
        denominator = 1
        for j in range(n):
            if i != j:
                numerator.append('(x - {})'.format(x_values[j]))
                denominator *= (x_values[i] - x_values[j])
        numerator_expression = '*'.join(numerator)
        coefficients[i] = '({})/{}'.format(numerator_expression, denominator)

    return coefficients

print("==========Respuestas pregunta 8==========")
points = [(0,1),(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
x_value=[0,1,2,3,4,5,6,7,8,9]
y_value=[1,2,3,4,5,6,7,8,9,10]

# # Base canónica
# canonical_polynomial = Pol_Interpolacion(x_value,y_value)
# print("Polinomio de interpolación usando la base canónica:")
# print(canonical_polynomial)

# # Base de Lagrange
# lagrange_polynomial = lagrange_interpolation(x_value,y_value)
# print("\nPolinomio de interpolación usando la base de Lagrange:")
# for i in range(len(lagrange_polynomial)):
#     if(i==len(lagrange_polynomial)-1) :print(y_value[i] , lagrange_polynomial[i])
#     else :print(y_value[i] , lagrange_polynomial[i] ,"+")

# # Base de Newton
# newton_polynomial = newton_interpolation(points)
# print("\nPolinomio de interpolación usando la base de Newton:")
# print(newton_polynomial)

print("==========Respuestas pregunta 9==========")
#Ejercicio 9
#Interpolacion de Hermite
def calcular_coeficientes_hermite(x, y, y_prime):
    n = len(x)
    coeficientes = [0.0] * (2 * n)
    
    for i in range(n):
        coeficientes[2 * i] = y[i]
        coeficientes[2 * i + 1] = y_prime[i]
        
        for j in range(2 * i - 1, -1, -1):
            coeficientes[j] = (coeficientes[j + 1] - coeficientes[j]) / (x[i] - x[j // 2])
    
    return coeficientes

def evaluar_polynomial(x, coeficientes, x_i):
    n = len(coeficientes) // 2
    result = coeficientes[2 * n - 1]
    
    for i in range(2 * n - 2, -1, -1):
        result = result * (x_i - x[i // 2]) + coeficientes[i]
    
    return result

def construir_polynomial_hermite(x, y, y_prime):
    coeficientes = calcular_coeficientes_hermite(x, y, y_prime)
    return lambda x_i: evaluar_polynomial(x, coeficientes, x_i)

print("==========Respuestas pregunta 10==========")
def Lagrange_interpolation(points):
    def L(k, x):
        result = 1
        for i, p  in enumerate(points):
            if i != k:
                result *= (x - p[0]) / (points[k][0] - p[0])
        return result

    def polynomial(x):
        result = 0
        for i, p in enumerate(points):
            result += p[1] * L(i, x)
        return result

    return polynomial

# Datos
point = [(0, 0, 75), (3, 225, 77), (5, 383, 80), (8, 623, 74), (13, 993, 72)]
points= [(0, 0), (3, 225), (5, 383), (8, 623), (13, 993)]
x_val=[0,3,5,8,13]
y_val=[0,225,383,623,993]
der_val=[75,77,80,74,72]

#Hermite 
poli=construir_polynomial_hermite(x_val, y_val,der_val)
#evaluarlo en 10
print("p(10) =", poli(10))
# Lagrange
interpolation_poly = Lagrange_interpolation(points)
# evaluar el polinomio en un punto
x = 10
print(f"El valor interpolado en x = {x} es: {interpolation_poly(x)}")

