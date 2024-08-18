import heapq
# Dada una lista de aristas, calcula el MST
# MST: Árbol Generador Mínimo
# O(M log M)
# Devuelve el costo y la lista de aristas del MST

def Prim(g : list[tuple[int,int,int]], start : int = 0) :
  # -> tuple[int, list[tuple[int,int,int]]]:
  heap = [(0,-1,start)]
  costo = 0
  mst = []
  n = max([a[0] for a in g] + [a[1] for a in g]) + 1
  adj = [[] for _ in range(n)]
  for a in g:
    adj[a[0]].append((a[1],a[2]))
    adj[a[1]].append((a[0],a[2]))
  used = [False] * n
  while heap:
    w,u,v = heapq.heappop(heap)
    if used[v]: continue
    used[v] = True
    if u != -1:
      costo += w
      mst.append((u,v,w))
    for x in adj[v]:
      if not used[x[0]]:
        heapq.heappush(heap,(x[1],v,x[0]))
  return costo, mst
