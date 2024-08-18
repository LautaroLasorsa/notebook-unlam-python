# https://cses.fi/problemset/task/2076
# https://cses.fi/problemset/task/2077

def Biconexas(g, ars):
  # -> tuple[list[int], list[bool], list[bool]] :
  # Primero: Componente biconexa de cada arista
  # Segundo: Para cada nodo, si es punto de articulación
  # Tercero: Para cada arista, si es puente
  n = len(g)
  m = len(ars)

  cmp = [-1] * m
  punto = [0] * n
  puente = [0] * m
  padre = [-1] * n

  llegada = [-1] * n
  min_alcanza = [-1] * n
  tiempo = 0
  pila = []
  indice = [0] * n
  componente = 0

  def DFS(u):
    nonlocal tiempo, componente
    pila_dfs = [u]
    while len(pila_dfs) > 0:
        u = pila_dfs.pop()

        if llegada[u] == -1:
            llegada[u] = tiempo
            min_alcanza[u] = tiempo
            tiempo += 1

        ar = g[u][indice[u]]
        v = ars[ar][0] + ars[ar][1] - u
        if ar != padre[u]:

            if llegada[v] == -1:
                padre[v] = ar
                pila_dfs.append(u)
                pila_dfs.append(v)
                pila.append(ar)
                continue

            if padre[v] == ar:
                if min_alcanza[v] > llegada[u]: puente[ar] = True
                if min_alcanza[v] >= llegada[u]:
                    punto[u] += 1
                    last = pila.pop()
                    while last != ar:
                        cmp[last] = componente
                        last = pila.pop()
                    cmp[ar] = componente
                    componente += 1
                min_alcanza[u] = min(min_alcanza[u], min_alcanza[v])
            elif llegada[v] < llegada[u]:
                pila.append(ar)
                min_alcanza[u] = min(min_alcanza[u], llegada[v])

        indice[u] += 1
        if indice[u] < len(g[u]):
            pila_dfs.append(u)
        continue

  for i in range(n):
    if padre[i] == -1:
      punto[i] -= 1
      DFS(i)

  punto = [punto[i] > 0 for i in range(n)]
  return cmp, punto, puente

n, m = map(int, input().split())
g = [[] for _ in range(n)]
ars = []
for i in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  g[u].append(i)
  g[v].append(i)
  ars.append((u,v))

cmp, punto, puente = Biconexas(g, ars)

# Para puentes (Necessary Roads)
if False:
    print(sum(puente))
    for i in range(m):
        if puente[i]:
            print(ars[i][0]+1,ars[i][1]+1)

# Para puntos de articulación (Necessary Cities)
else :
    print(sum(punto))
    for i in range(n):
        if punto[i]:
            print(i+1)
    



