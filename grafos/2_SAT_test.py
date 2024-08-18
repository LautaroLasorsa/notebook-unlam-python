# https://cses.fi/problemset/task/1684

def Tarjan(g):
    n = len(g)
    cmp = [-1] * n
    cmp_id = 0
    tiempo = 0

    entrada = [-1] * n
    min_entrada = [-1] * n
    arista = [0]*n
  
    def dfs(u):
        nonlocal cmp_id
        nonlocal tiempo

        pila = [u]
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
                    min_entrada[u] = min(min_entrada[u], min_entrada[v])
                elif cmp[v] == -1:
                    min_entrada[u] = min(min_entrada[u], entrada[v])
                arista[u] += 1
            if arista[u] == len(g[u]) and entrada[u] == min_entrada[u]:
                while True:
                    v = pila_cmp.pop()
                    cmp[v] = cmp_id
                    if v == u: break
                cmp_id += 1

    for u in range(n):
        if cmp[u] == -1:
            dfs(u)
    return cmp


def Toposort(g):
  n = len(g)
  deg = [0]*n
  for u in range(n):
    for v in g[u]:
      deg[v] += 1
  q = [u for u in range(n) if deg[u] == 0]
  res = []
  while len(q) > 0:
    u = q.pop()
    res.append(u)
    for v in g[u]:
      deg[v] -= 1
      if deg[v] == 0:
        q.append(v)
  return res

def Condensado(g):
  cmp = Tarjan(g) # Puede ser Kosaraju
  n_cmp = max(cmp)+1
  gc = [[] for _ in range(n_cmp)]
  for u in range(len(g)):
    for v in g[u]:
      if cmp[u] != cmp[v]:
        gc[cmp[u]].append(cmp[v])
  for u in range(n_cmp):
    gc[u] = list(set(gc[u]))
  return (gc, cmp)

def SAT2(n , f): # Formato input: >0 afirmo variable, <0 niego variable
  g = [[] for _ in range(2*n)]

  def neg(x):
    return x+n if x<n else x-n

  # Construyo el grafo de implicancias que modela el problema
  for (p1, p2) in f:
    x1 = p1 - 1 if p1>0 else neg(-p1-1)
    x2 = p2 - 1 if p2>0 else neg(-p2-1)
    g[neg(x1)].append(x2)
    g[neg(x2)].append(x1)

  # Calculo el grafo condensado
  (gc, cmp) = Condensado(g)
  componentes = [[] for _ in range(len(gc))]
  for u in range(2*n):
    componentes[cmp[u]].append(u)

  # Reviso que no haya contradicción
  for i in range(n):
    if cmp[i]==cmp[i+n]:
      return []

  # Asigno valores a las variables
  res = [-1] * n

  orden = Toposort(gc)

  for U in reversed(orden):
    for u in componentes[U]:
      x = u if u<n else neg(u)
      if res[x]==-1:
        res[x] = u<n

  return res

m,n = map(int, input().split())
fs = []
for _ in range(m):
    su, u, sv, v = input().split()
    u, v = int(u), int(v)
    if su == "-":
        u = -u
    if sv == "-":
        v = -v
    fs.append((u,v))
# print(fs)
res = SAT2(n, fs)
if not res:
    print("IMPOSSIBLE")
else:
    print(" ".join(["+" if r else "-" for r in res])) 