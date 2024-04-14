import numpy as np

def plu_factorization(A):
    n = A.shape[0]
    P = np.eye(n)  # Inicializamos la matriz de permutación como la matriz identidad
    L = np.zeros((n, n))  # Inicializamos la matriz triangular inferior
    U = A.copy()  # Inicializamos la matriz triangular superior como una copia de la matriz original

    for j in range(n - 1):
        # Buscamos el pivote máximo en la columna j
        pivot_row = np.argmax(np.abs(U[j:, j])) + j

        # Intercambiamos las filas de U y P
        if pivot_row != j:
            U[[j, pivot_row], :] = U[[pivot_row, j], :]
            P[[j, pivot_row], :] = P[[pivot_row, j], :]

        # Actualizamos las matrices L y U
        L[j+1:, j] = U[j+1:, j] / U[j, j]
        U[j+1:, j:] -= np.outer(L[j+1:, j], U[j, j:])
    
    # L tiene unos en la diagonal
    np.fill_diagonal(L, 1)

    return P, L, U

# Ejemplo de uso
A = np.array([[2, 1, -1],
              [4, 3, 3],
              [4, 1, -3]])

P, L, U = plu_factorization(A)
print("Matriz de permutación P:")
print(P)
print("\nMatriz triangular inferior L:")
print(L)
print("\nMatriz triangular superior U:")
print(U)