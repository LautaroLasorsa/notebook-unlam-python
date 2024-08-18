# Dada una lista de aristas, calcula el MST
# MST: Árbol Generador Mínimo
# Notar que es necesario implementar también un union find
# O(M log M)
# Devuelve el costo y la lista de aristas del MST

def Kruskal(g : list[tuple[int,int,int]]): 
    # -> tuple[int, list[tuple[int,int,int]]]:
    g.sort(key=lambda x: x[2])
    global n, id, cmp
    n = max([a[0] for a in g] + [a[1] for a in g]) + 1
    id = [i for i in range(n)]
    cmp = [[i] for i in range(n)]
    cost = 0
    mst = []
    for a in g:
        if union(a[0], a[1]):
        # usemos el union-find que nos guste
            cost += a[2]
            mst.append(a)
    return cost, mst