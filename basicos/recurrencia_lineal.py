# Problema: Dada una recurrencia lineal de la forma
# A[i] = c1 * A[i - 1] + c2 * A[i - 2] + ... + ck * A[i - k]
# con A[0], A[1], ..., A[k - 1] dados, determinar A[n] para n >= k.
# ej: Fibonacci(n) = recurrencia([0,1],[1,1],n)
# IMPORTANTE: no olvidar el modulo

def recurrencia(A, C, n, mod = int(1e9+7)): # O(n * k)
    k = len(C)
    if n < k:
        return A[n]
    A = A + [0] * (n - k + 1)
    for i in range(k, n + 1):
        A[i] = sum(C[j] * A[i - j] for j in range(k)) % mod
    return A[n]

# No lo vimos en clase, pero existe una solución más eficiente en O(k^2 * log(n)) usando exponenciación binaria de polinomios.
def recurrencia(A, C, n, mod = int(1e9+7)): # O(k^2 * log(n))
    k = len(C)
    if n < k:
        return A[n]
    A = A + [0] * (n - k + 1)
    def mult(A, B): # Producto de polinomios 
        n = len(A)
        C = [0] * n
        for i in range(n):
            for j in range(n):
                C[i] += A[j] * B[i - j]
                C[i] %= mod
        return C
    def exp(A, n): # Potencia rápida de polinomios
        if n == 1:
            return A
        if n % 2 == 0:
            return exp(mult(A, A), n // 2)
        return mult(A, exp(A, n - 1))
    C = [0] * (k * k)
    for i in range(k):
        C[i * k + i] = 1
    C = exp(C, n - k)
    for i in range(k):
        A[n] += C[i] * A[k - i]
        A[n] %= mod
    return A[n]
