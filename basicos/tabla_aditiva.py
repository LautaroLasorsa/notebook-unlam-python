def crear(V):
    n = len(V)
    A = [0] * (n + 1)
    for i in range(n):
        A[i + 1] = A[i] + V[i]
    return A #A[i] = sum(V[:i))

def consulta(A, l, r):
    return A[r] - A[l] #sum(V[l:r))