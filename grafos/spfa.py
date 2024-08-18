# Modificación de BellmanFord
# Calcula la distancia desde el origen a todos los demás nodos
# Soporta pesos negativos
# En el caso promedio: O(N + M)
# En el peor caso: O(N * M)

def SPFA(origen : int, G : list[list[tuple[int,int]]]) -> list[int]:
  distancias = [float('inf')] * len(G)
  distancias[origen] = 0
  cola = [origen]
  i = 0
  en_cola = [False] * len(G)
  while i < len(cola):
    u = cola[i]
    en_cola[u] = False
    for v, w in G[u]:
      if distancias[v] > distancias[u] + w:
        distancias[v] = distancias[u] + w
        if not en_cola[v]:
          cola.append(v)
          en_cola[v] = True
    i += 1
  return distancias