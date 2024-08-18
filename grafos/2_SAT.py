# Problema de 2-Satisfactibilidad

# Dada una fórmula en forma normal conjuntiva (CNF) 
# con 2 variables por cláusula,
# determinar si existe una asignación de valores a 
# las variables que haga verdadera
# a la fórmula.
# La fórmula se representa como una lista de cláusulas, 
# donde cada cláusula es una
# tupla de dos elementos. Si el primer elemento de la 
# tupla es positivo, se afirma la variable correspondiente. 
# Si el segundo elemento de la tupla es positivo, se
# afirma la variable correspondiente. Si el primer elemento 
# de la tupla es negativo, se niega la variable correspondiente. 
# Si el segundo elemento de la tupla es negativo, se niega la 
# variable correspondiente.

# La función retorna una lista de booleanos, donde el i-ésimo 
# booleano indica si la variable i debe ser verdadera o falsa. 
# Si no existe una  asignación que haga verdadera a la fórmula, 
# retorna una lista vacía.
# La función tiene complejidad O(N+M), donde 
# N es el número de variables y 
# M es el número de cláusulas.
# Ejemplo de uso:
# f = [(1,2),(-1,-2),(1,-2),(-1,2)]
# print(SAT2(2,f)) # [True, True]
# print(SAT2(2,[(1,2),(1,-2),(-1,2),(-1,-2)])) # []
# Necesita tener implementado Condensado y Toposort

def SAT2(n : int, f : list[tuple[int,int]]) -> list[bool]: 
  # Formato input: >0 afirmo variable, <0 niego variable
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
