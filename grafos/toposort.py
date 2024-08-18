# Dado un DAG (Grafo Dirigido Aciclico)
# genera el orden topologico del grafo
# (una permutacion de los nodos tal que si hay una arista
# de u a v, entonces u aparece antes que v en la permutacion)
# Si el grafo no es un DAG, el resultado no tiene sentido
# O(N+M) tiempo

def Toposort(g : list[list[int]]) -> list[int]:
  n = len(g)
  deg = [0]*n
  for u in range(n):
    for v in g[u]:
      deg[v] += 1
  q = [u for u in range(n) if deg[u] == 0]
  res = []
  while len(q) > 0:
    u = q.pop()
    res.append(u)
    for v in g[u]:
      deg[v] -= 1
      if deg[v] == 0:
        q.append(v)
  return res