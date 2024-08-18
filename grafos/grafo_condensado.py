# Dado un grafo dirigido g, retorna el grafo condensado
# de g y la componente fuertemente conexa de cada nodo
# Recordar: El grafo condensado de G es aquel en el que
# cada componente fuertemente conexa de G es un nodo
# y hay una arista de un nodo U a otro V si en G hay
# una arista de un nodo u en U a un nodo v en V
# Requiere Tarjan o Kosaraju ya implementado
# O(N+M) tiempo

def Condensado(g : list[list[int]]) -> list[list[int]]:
  cmp = Tarjan(g) # Puede ser Kosaraju
  n_cmp = max(cmp)+1
  gc = [[] for _ in range(n_cmp)]
  for u in range(len(g)):
    for v in g[u]:
      if cmp[u] != cmp[v]:
        gc[cmp[u]].append(cmp[v])
  for u in range(n_cmp):
    gc[u] = list(set(gc[u]))
  return (gc, cmp)