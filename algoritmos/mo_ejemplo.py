# Utilizar el algoritmo de Mo para resolver
# el problema de responder consultas de suma
# en rango sobre un vector V de enteros sin 
# actualizaciones
# O((N+Q) * sqrt(N))

def SumaEnRango(V : list[int], L : list[int], R:list[int]) -> list[int]:
  N, Q = len(V), len(R)
  queries = [(L[i], R[i], i) for i in range(Q)]
  BASE = int(N**0.5+1)
  res = [0] * Q
  queries.sort(key=lambda x: (x[0]//BASE, x[1]))
  i, j, suma = 0, 0, 0
  for l, r, idx in queries:
    while i < l:
      suma -= V[i]
      i += 1
    while i > l:
      i -= 1
      suma += V[i]
    while j < r:
      suma += V[j]
      j += 1
    while j > r:
      j -= 1
      suma -= V[j]
    res[idx] = suma
  return res