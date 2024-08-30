# Computa para cada nodo de un árbol
# el tiempo de entrada y la profundidad
# y construye un vector a tal que 
# min(a[in[u]:in[v]+1]) es el par ordenado
# (in[c],c), donde c es el LCA de u y v


def generar(g : list[list[int]], raiz : int = 0) \
    -> tuple[list[int], list[int], list[int]]:
    n = len(g)
    in_order = [-1]*n
    depth = [0]*n
    a_vec = []
    arista = [0] * n
    pila = [raiz]
    while pila:
        u = pila[-1]
        pila.pop()
        if in_order[u] == -1:
            in_order[u] = len(a_vec)
        a_vec.append((in_order[u],u))
        if arista[u] < len(g[u]):
            v = g[u][arista[u]]
            arista[u] += 1
            if in_order[v] == -1:
                depth[v] = depth[u] + 1
                pila.append(u)
                pila.append(v)
    return in_order, depth, a_vec

def operation(a, b):
    return min(a,b)

def next_p2(n: int) -> int:
    return 1 << (n - 1).bit_length()

# Función que recibe un vector y construye su Sparse Table
# O(NlogN)
def st_build(v):
    n = len(v)
    k = n.bit_length()
    st = [[0] * k for _ in range(n)]
    for i in range(n):
        st[i][0] = v[i]
    for j in range(1, k):
        for i in range(n - (1 << j) + 1):
            st[i][j] = operation(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
    return st

# O(1): Usar si la operación es idempotente (ej: mínimo, máximo, and, or)
def st_query(st, l : int, r : int):
    j = r - l
    k = j.bit_length() - 1
    return operation(st[l][k], st[r - (1 << k)][k])

# Usa Sparse Table
class LCA_ST:
    # O(NlogN)
    def __init__(self, g , raiz : int = 0):
        self.n = len(g)
        self.in_order, self.depth, self.a_vec = generar(g, raiz)
        self.st = st_build(self.a_vec)
    
    def lca(self, u : int, v : int) -> int:
        l, r = self.in_order[u], self.in_order[v]
        if l > r:
            l, r = r, l
        return st_query(self.st, l, r)[1]
    
