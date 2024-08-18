# Solución al problema Cambio de Monedas con DP
# Problema: Dado un conjunto de monedas C = {c1, c2, ..., ck} y un valor V, determinar el mínimo número de monedas de C necesarias para sumar V.
def cambio_monedas(C, V): #O(n * V)
    n = len(C)
    A = [0] + [float('inf')] * V
    for i in range(1, V + 1):
        for j in range(n):
            if i >= C[j]:
                A[i] = min(A[i], A[i - C[j]] + 1)
    return A # A[i] = mínimo número de monedas de C necesarias para sumar i
