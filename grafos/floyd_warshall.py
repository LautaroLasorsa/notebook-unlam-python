# Calcula la distancia mínima de cada nodo a cada nodo
# Soporta pesos negativos
# Retorna una matriz de distancias
# O(N^3)
def FloydWarshall(G : list[list[tuple[int,int]]]):
  distancias = [[float('inf')] * len(G) for _ in range(len(G))]
  for u in range(len(G)):
    distancias[u][u] = 0
    for v, w in G[u]:
      distancias[u][v] = w

  for k in range(len(G)):
    for i in range(len(G)):
      for j in range(len(G)):
        distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

  return distancias