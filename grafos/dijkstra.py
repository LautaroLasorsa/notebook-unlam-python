import heapq

# Implementación O(M * log N) de Dijkstra con heap
# Es en casi todo caso lo recomendable
# Recibe un nodo de origen y una lista de adyacencia
# Devuelve la distancia mínima de origen a cada nodo
# float('inf') si no es alcanzable
# Funciona tanto para ponderado como para no ponderado
# Recordar que Dijkstra no soporta pesos negativos

def DijkstraHeap(origen : int, G : list[list[tuple[int,int]]]):
  distancias = [float('inf')] * len(G)
  distancias[origen] = 0
  procesados = [False] * len(G)

  heap = []
  heapq.heappush(heap, (0, origen))
  while heap:
    dist, nodo = heapq.heappop(heap)
    if procesados[nodo]:
      continue
    procesados[nodo] = True
    for (vecino, distancia) in G[nodo]:
      if distancias[vecino] > distancias[nodo] + distancia:
        distancias[vecino] = distancias[nodo] + distancia
        heapq.heappush(heap, (distancias[vecino], vecino))

  return distancias

# Implementación O(N^2) de Dijkstra
# Solo recomendable en grafos densos donde M ~ N^2
# Recibe y devuelve o mismo que la implementación anterior.
def DijkstraCuadratico(origen : int, G : list[list[tuple[int,int]]]):
  distancias = [float('inf')] * len(G)
  distancias[origen] = 0
  procesados = [False] * len(G)
  for _ in range(len(G)):
    siguiente = -1
    for i in range(len(G)):
      if not procesados[i] and (siguiente == -1 or distancias[i] < distancias[siguiente]):
        siguiente = i
    if siguiente == -1:
      break
    procesados[siguiente] = True
    for (vecino, distancia) in G[siguiente]:
      if not procesados[vecino] and distancias[vecino] > distancias[siguiente] + distancia:
        distancias[vecino] = distancias[siguiente] + distancia

  return distancias
