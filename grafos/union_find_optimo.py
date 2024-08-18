# Implementa union find con las optimizaciones
# de path compression y union by size comentadas
# en la clase
# Notar que n se debe definir antes en el código

pad = [i for i in range(n)] 
# Inicialmente cada nodo es su propio padre
sz = [1] * n 
# tamaño de las componentes

def find(u):
    visto = []
    while u != pad[u]:
        visto.append(u)
        u = pad[u]
    for x in visto:
        pad[x] = u
    return u

# Retorna True si se unieron los nodos,
# False si ya estaban en la misma componente
def union(u, v):
    u, v = find(u), find(v)
    if u == v: return False
    if sz[u] < sz[v]: u, v = v, u
    pad[v] = u
    sz[u] += sz[v]
    return True