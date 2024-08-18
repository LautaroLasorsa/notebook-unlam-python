# Problema: Dado un árbol, encontrar un matching de tamaño
# máximo. Recordar que un matching es un conjunto de aristas
# tal que no hay dos aristas incidentes en el mismo nodo.
# O(N)

def Matching(arbol : list[list[int]]) -> list[tuple[int,int]]:
  N = len(arbol)
  orden, dist = OrdenarNodos(0, arbol)
  pareja = [-1]*N
  matching = []
  for nodo in orden:
    for vecino in arbol[nodo]:
      if dist[vecino] > dist[nodo] and pareja[vecino] == -1: 
# verificar que sea su hijo (tenga mayor distancia a la raiz) y no tenga pareja
        pareja[vecino] = nodo
        pareja[nodo] = vecino
        matching.append((nodo,vecino))
        break # ya no necesita ver a sus demás hijos
  return matching