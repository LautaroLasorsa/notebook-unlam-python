# Recibe una raíz y una lista de adyacencia de un árbol
# Nos da la profundidad (distancia a la raíz) de cada nodo
# y los nodos ordenados por profundidad (desempate arbitrario)
# O(N)
# Altura = max(dist)

def OrdenarNodos(raiz : int, ady:list[list[int]])->tuple[list[int],list[int]]:
  inf = int(1e9) # Representa una distancia infinita
  N = len(ady)
  dist = [inf]*N
  dist[raiz] = 0
  bolsa, it = [raiz], 0
  while it < len(bolsa):
    nodo = bolsa[it]
    for vecino in ady[nodo]:
      if dist[vecino]>dist[nodo]+1:
        dist[vecino] = dist[nodo]+1
        bolsa.append(vecino)
    it = it+1
  return (reversed(bolsa), dist)
  # Si notamos, la bolsa del algoritmo BFS nos da el orden que queremos, pero al revez.
  # Además, en el proceso obtuvimos la distancia de cada nodo a la raiz, 
  # es decir su profundidad