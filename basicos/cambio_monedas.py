# Solución al problema Cambio de Monedas con DP
# Problema: Dados: 
#   * un conjunto de monedas C = {c1, c2, ..., ck}
#   * Un valor V, 
# Determinar el mínimo número de monedas de C necesarias para sumar V.
def cambio_monedas(C, V): #O(n * V)
    n = len(C)
    A = [0] + [float('inf')] * V
    for i in range(1, V + 1):
        for j in range(n):
            if i >= C[j]:
                A[i] = min(A[i], A[i - C[j]] + 1)
    return A 
# A[i] = mínimo número de monedas de C necesarias para sumar i
