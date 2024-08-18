def Tarjan(g : list[list[int]]) -> list[int] :
  n = len(g)
  cmp = [-1] * n
  cmp_id = 0
  pila = []
  tiempo = 0

  entrada = [-1] * n
  min_entrada = [-1] * n

  arista = [0]*n
  def dfs(u : int):
    nonlocal cmp_id
    nonlocal tiempo
    pila = [u]
    entrada[u] = tiempo
    min_entrada[u] = tiempo
    tiempo += 1
    pila_cmp = []
    while pila:
      u = pila[-1]
      pila.pop()
      if entrada[u] == -1:
        entrada[u] = tiempo
        min_entrada[u] = tiempo
        tiempo += 1
        pila_cmp.append(u)

      while arista[u] < len(g[u]):
        v = g[u][arista[u]]
        if entrada[v] == -1:
          pila.append(u)
          pila.append(v)
          break 
        elif entrada[v] > entrada[u]:
          min_entrada[u] = min(min_entrada[u], min_entrada[u])
        elif cmp[v] == -1:
          min_entrada[u] = min(min_entrada[u], entrada[v])
        arista[u] += 1
      
      if entrada[u] == min_entrada[u]:
        while True:
          v = pila_cmp.pop()
          cmp[v] = cmp_id
          if v == u: break
        cmp_id += 1

  for u in range(n):
    if cmp[u] == -1:
      dfs(u)

  return cmp