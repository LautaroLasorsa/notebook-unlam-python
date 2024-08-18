# Dado un grafo con aristas con etiquetas 0 y 1
# * Las etiquetas 0 indican que ambos nodos deben tener el mismo color
# * Las etiquetas 1 indican que ambos nodos deben tener colores distintos
# Decide si es posible colorear el grafo con dos colores
# de tal forma que se cumplan todas las etiquetas
# Si se puede, retorna True y la lista de colores
# Si no, retorna False y una lista vacía

def Bipartir2(ady: list[tuple[int,int]]) -> tuple[bool, list[int]] :
  # arista es (vecino, peso)
  N = len(ady)
  color = [-1]*N
  for inicio in range(0,N):
    if color[inicio] != -1: continue
    color[inicio] = 0
    bolsa, it = [inicio], 0
    while it < len(bolsa):
      nodo = bolsa[it]
      for vecino, peso in ady[nodo]:
        if color[vecino]==-1:
          color[vecino] = peso ^ color[nodo]
          bolsa.append(vecino)
        elif color[vecino] == color[nodo] ^ peso:
          return (False, [])

      it = it+1
  return (True,color)