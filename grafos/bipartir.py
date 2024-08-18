# Decide si un grafo puede ser bipartito
# Es decir, asignar a cada nodo uno de dos colores
# de tal forma que no haya dos nodos vecinos del mismo color
# Si se puede, retorna True y la lista de colores
# Si no, retorna False y una lista vacía 

def Bipartir(ady:list[list[int]])->tuple[bool,list[int]]:
  N = len(ady)
  color = [-1]*N
  for inicio in range(0,N):
    if color[inicio] != -1: continue
    color[inicio] = 0
    bolsa, it = [inicio], 0
    while it < len(bolsa):
      nodo = bolsa[it]
      for vecino in ady[nodo]:
        if color[vecino]==-1:
          color[vecino] = 1-color[nodo]
          bolsa.append(vecino)
        elif color[vecino]==color[nodo]:
          return (False,[])
      it = it+1
  return (True,color)