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

# Usa Sparse Table
class LCA_ST:
    # O(NlogN)
    def __init__(self, g : list[list[int]], raiz : int = 0):
        self.n = len(g)
        self.in_order, self.depth, self.a_vec = generar(g, raiz)
        self.st = st_build(self.a_vec)
    
    def lca(self, u : int, v : int) -> int:
        l, r = self.in_order[u], self.in_order[v]
        if l > r:
            l, r = r, l
        return st_query(self.st, l, r)[1]