# Recorrido de BFS de un grafo
# Recibe la lista de adyacencia y un nodo de origen
# Devuelve la distancia del origen a cada nodo
# inf para nodos inalcanzables
def BFS(inicio : int, ady:list[list[int]])->list[int]:
  N = len(ady)
  dist = [float('inf')]*N
  dist[inicio] = 0
  bolsa, it = [inicio], 0
  while it < len(bolsa):
    nodo = bolsa[it]
    for vecino in ady[nodo]:
      if dist[vecino]>dist[nodo]+1:
        dist[vecino] = dist[nodo]+1
        bolsa.append(vecino)
    it = it+1
  return dist