# Indentifica los puentes, puntos de articulación y componentes
# biconexas de un grafo no dirigido, recibiendo la lista de incidencia
# g y la lista de aristas ars (cada arista es una tupla de dos nodos)
# Puente: Arista que si elimina aumentan lac antidad de componentes
# conexas del grafo
# Punto de articulación: Nodo que si se elimina aumenta la cantidad
# de componentes conexas del grafo
# Componente biconexa: Subgrafo conexo que no tiene puntos de 
# articulación.
# Notar que la división en componentes biconexas es una partición 
# de las aristas del grafo (cada arista pertenece a una unica 
# componente biconexa) pero no de los nodos, los puntos de 
# articulación pertenecen a más de una componente biconexa
# O(N+M) tiempo

def Biconexas(g : list[list[int]], ars : list[tuple[int,int]]):
  # -> tuple[list[int], list[bool], list[bool]] :
  # Primero: Componente biconexa de cada arista
  # Segundo: Para cada nodo, si es punto de articulación
  # Tercero: Para cada arista, si es puente
  n = len(g)
  m = len(ars)

  cmp = [-1] * m
  punto = [0] * n
  puente = [0] * m
  padre = [-1] * n

  llegada = [-1] * n
  min_alcanza = [-1] * n
  tiempo = 0
  pila = []
  indice = [0] * n
  componente = 0

  def DFS(u):
    nonlocal tiempo, componente
    pila_dfs = [u]
    while len(pila_dfs) > 0:
        u = pila_dfs.pop()

        if llegada[u] == -1:
            llegada[u] = tiempo
            min_alcanza[u] = tiempo
            tiempo += 1

        ar = g[u][indice[u]]
        v = ars[ar][0] + ars[ar][1] - u
        if ar != padre[u]:

            if llegada[v] == -1:
                padre[v] = ar
                pila_dfs.append(u)
                pila_dfs.append(v)
                pila.append(ar)
                continue

            if padre[v] == ar:
                if min_alcanza[v] > llegada[u]: puente[ar] = True
                if min_alcanza[v] >= llegada[u]:
                    punto[u] += 1
                    last = pila.pop()
                    while last != ar:
                        cmp[last] = componente
                        last = pila.pop()
                    cmp[ar] = componente
                    componente += 1
                min_alcanza[u] = min(min_alcanza[u], min_alcanza[v])
            elif llegada[v] < llegada[u]:
                pila.append(ar)
                min_alcanza[u] = min(min_alcanza[u], llegada[v])

        indice[u] += 1
        if indice[u] < len(g[u]):
            pila_dfs.append(u)
        continue

  for i in range(n):
    if padre[i] == -1:
      punto[i] -= 1
      DFS(i)

  punto = [punto[i] > 0 for i in range(n)]
  return cmp, punto, puente


