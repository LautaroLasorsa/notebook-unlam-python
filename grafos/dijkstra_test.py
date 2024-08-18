# https://cses.fi/problemset/task/1671
import heapq
def DijkstraHeap(origen, G):
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
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int,input().split())
    g[a-1].append((b-1,c))

for d in DijkstraHeap(0,g):
  print(d, end=" ")
