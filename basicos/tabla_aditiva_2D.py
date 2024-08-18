# Permite crear y consultar una tabla aditiva para matrices 2D en O(n * m) y O(1) respectivamente.
def crear(M): #M: matriz, O(n * m)
    n, m = len(M), len(M[0])
    A = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            A[i + 1][j + 1] = A[i + 1][j] + A[i][j + 1] - A[i][j] + M[i][j]
    return A #A[i][j] = sum(M[:i)[:j))

def consulta(A, l1, r1, l2, r2): #O(1)
    return A[r1][r2] - A[l1][r2] - A[r1][l2] + A[l1][l2] #sum(M[l1:r1)[:l2:r2))