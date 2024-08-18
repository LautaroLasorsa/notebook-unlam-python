# Notar que el codigo no cambia si el grafo es ponderado o no
def leer_lista_aristas(m):
    return [
        list(map(lambda x : int(x)-1, input().split()))
        for _ in range(m)
    ]

# ady[u] son los nodos a los que llegan aristas desde u
def leer_lista_adyacencia(n,m):
    # reutilizo código
    aristas = leer_lista_aristas(m)
    ady = [[] for _ in range(n)]
    for arista in aristas:
        u = arista[0]
        v = arista[1]

        # Para grafo ponderado 
        ady[u].append([v]+arista[1:])
        ady[v].append([v]+arista[1:]) # no dirigido
        
        # Para grafo no ponderado
        ady[u].append(v)
        ady[v].append(u) # no dirigido

    return ady

# inc[u] son las aristas incidentes al nodo u
def leer_lista_incidencia(n,m):
    aristas = leer_lista_aristas(m)
    inc = [[] for _ in range(n)]
    for i,arista in enumerate(aristas):
        u = arista[0]
        v = arista[1]
        inc[u].append(i)
        inc[v].append(i) # no dirigido
    return inc, aristas

