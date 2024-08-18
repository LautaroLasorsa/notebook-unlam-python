# Ejemplo de problema resuelto con D&C
# Ordena un vector en O(nlogn)
# Realiza log(n) capas de recursión
def MergeSort(V : list[any]) -> list[any] :
  if len(V) < 2: return V
  m = len(V) // 2
  L = MergeSort(V[:m])
  R = MergeSort(V[m:])
  i,j = 0,0
  for k in range(len(V)):
    if i >= len(L):
      V[k] = R[j]
      j += 1
    elif j >= len(R):
      V[k] = L[i]
      i += 1
    elif L[i] < R[j]:
      V[k] = L[i]
      i += 1
    else:
      V[k] = R[j]
      j += 1
  return V