# Calcular el mínimo entero no negativo excluido
# de un iterable.
# Importante porque el número de Grundy de un estado
# de un juego es el MEX de los Grundy de los estados
# a los que se puede llegar.
# O(N)

def MEX(iterable):
  n = len(iterable)
  esta = [False] * (n+1)
  for i in iterable:
    if i <= n:
      esta[i] = True
  mex = 0
  while mex<n and esta[mex]:
    mex += 1
  return mex

# Versión más corta pero menos performante
# por utilizar un set 
def MEX_byCopilot(iterable):
  mex = 0
  conjunto = set(iterable)
  while mex in conjunto:
    mex += 1
  return mex