# Ejemplo del uso de la técnica de ventana deslizante
# para resolver el problema de:
# Dado un arreglo de enteros V y un entero k
# determinar para cada subarreglo de longitud k
# la cantidad de elementos distintos
# O(N * acceso_diccionario)

def Distintos(V : list[int],k : int) -> list[int]:
  res = [0] * (len(V)-k+1)
  histo = dict()
  cantidad = 0
  for i in range(k):
    cantidad += 1 if V[i] not in histo else 0
    histo[V[i]] = histo.get(V[i],0) + 1
  res[0] = cantidad
  for i in range(1, len(V)-k+1):
    j = i+k
    cantidad -= 1 if histo.get(V[i],0) == 1 else 0
    cantidad += 1 if histo.get(V[j-1],0) == 0 else 0
    histo[V[i]] = histo.get(V[i],0) - 1
    histo[V[j-1]] = histo.get(V[j-1],0) + 1
    res[i] = cantidad
  return res