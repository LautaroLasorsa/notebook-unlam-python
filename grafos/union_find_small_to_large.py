# Implementa union find utilizando la técnica de
# small to large
# Notar que n se debe definir antes en el código

id = [i for i in range(n)] 
# Inicialmente cada nodo esta en su propia componente
cmp = [[i] for i in range(n)]

# Retorna True si se unieron los nodos,
# False si ya estaban en la misma componente
def union(u, v):
    u, v = id[u], id[v]
    if u == v: return False # No se los unio
    if len(cmp[u]) < len(cmp[v]): u, v = v, u
    for x in cmp[v]:
        cmp[u].append(x)
        id[x] = u
    return True