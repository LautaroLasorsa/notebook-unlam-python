# Recibe la lista de adyacencia de un grafo dirigido
# Devuelve una lista con el id de la componente
# fuertemente conexa a la que pertenece cada nodo
# O(N+M) tiempo 

def Kosaraju(g : list[list[int]]) -> list[int] :
    n = len(g)
    ord = []

    # Ordeno usando simil BFS
    d_in = [0] * n
    for u in range(n):
        for v in g[u]:
            d_in[v] += 1
    
    visitados = [False] * n
    arista = [0] * n
    
    # Hago un pseudo-toposort con DFS iterativo
    def dfs(ini):
        pila = [ini]
        while pila:
            u = pila.pop()
            visitados[u] = True
            
            while arista[u] < len(g[u]):
                v = g[u][arista[u]]
                arista[u] += 1
                if not visitados[v]:
                    pila.append(u)
                    pila.append(v)
                    break

            if arista[u] == len(g[u]):
                ord.append(u)
   
    for u in range(n):
        if not visitados[u]:
            dfs(u)
    
    # Transpongo el grafo
    gt = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            gt[v].append(u)

    # En el transpuesto recorro según el orden inverso de salida de DFS
    cmp = [-1] * n
    cmp_id = 0

    def marcar_componente(u : int):
        pila = [u]
        while pila:
            u = pila.pop()
            if cmp[u] != -1: continue
            cmp[u] = cmp_id
            for v in gt[u]:
                if cmp[v] == -1:
                    pila.append(v)

    # Recorro el grafo
    for u in reversed(ord):
        if cmp[u] == -1:
            marcar_componente(u)
            cmp_id += 1

    return cmp