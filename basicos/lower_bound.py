# Devuelve el índice del primer elemento mayor o igual a x 
# en un arreglo ordenado
def lower_bound(V, x):
    l, r = -1, len(V)
    while l < r: # V[l] < x <= V[r]
        m = (l + r) // 2
        if V[m] < x:
            l = m
        else:
            r = m
    return r