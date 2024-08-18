# La técnica de los dos punteros se utiliza
# para resolver problemas que trabajan con
# el conjunto de subarreglos de un arreglo que
# cumplen una propiedad X tal que si un subarreglo
# cumple la propiedad X, cualquier subarreglo
# que contenga al subarreglo también cumple la
# propiedad X.

# Ejemplo de problema resuelto con dos punteros
# Dado un arreglo de enteros no negativos V y 
# un entero k, determinar la cantidad de 
# subarreglos de V que suman al menos k.

def DosPunteros(V : list[int],k : int) -> int:
  res, suma = 0, 0
  L = 0
  for R in range(1,len(V)+1):
    suma += V[R-1]
    while R > L and suma >= k:
      suma -= V[L]
      L += 1
    res += R-L
  return res