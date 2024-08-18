# Recibe un nodo de origen, una lista de adyacencia y una longitud L
# Calcula para cada nodo y longitud la distancia mínima del origen a
# ese nodo con exactamente esa cantidad de aristas.
# Soporta pesos negativos.
# O((N+M) * L) tiempo, O(N*L) memoria

def BellmanFord(origen : int, G : list[list[tuple[int,int]]], L : int) -> list[list[int]]:
  distancias = [ [float('inf')] * len(G) for _ in range(L+1) ]
  distancias[0][origen] = 0
  for l in range(L):
    for u in range(len(G)):
      for v, w in G[u]:
        distancias[l+1][v] = min(distancias[l+1][v], distancias[l][u] + w)
  return distancias

# Similar a la anterior pero retorna para cada nodo
# la minima distancia del origen.
# Garantiza que probo al menos todos los caminos de L aristas o menos.
# O((N+M) * L) tiempo pero O(N) memoria
def BellmanFordLigero(origen : int, G : list[list[tuple[int,int]]], L : int) -> list[int]:
  distancias = [float('inf')] * len(G)
  distancias[origen] = 0
  for l in range(L):
    for u in range(len(G)):
      for v, w in G[u]:
        distancias[v] = min(distancias[v], distancias[u] + w)
  return distancias