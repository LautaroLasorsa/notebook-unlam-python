# Solución al Problema Sub Set Sum
# Problema: Dado un conjunto de enteros positivos C = {c1, c2, ..., ck} y un valor V, determinar si es posible sumar exactamente V usando elementos de C.
def sub_set_sum(C, V): #O(n * V)
    n = len(C)
    A = [False] * (V + 1)
    A[0] = True
    for i in range(n):
        for j in range(V, C[i] - 1, -1):
            A[j] |= A[j - C[i]]
    return A #A[i] = True si es posible sumar exactamente i usando elementos de C