# https://cses.fi/problemset/task/1683
import sys
sys.setrecursionlimit(10**6)
def Kosaraju(g) :
    n = len(g)
    ord = []

    # Ordeno usando simil BFS
    d_in = [0] * n
    for u in range(n):
        for v in g[u]:
            d_in[v] += 1
    
    visitados = [False] * n
    arista = [0] * n
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
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    g[u-1].append(v-1)

cmp = Kosaraju(g)
print(max(cmp)+1)
for c in cmp:
    print(c+1,end=" ")
