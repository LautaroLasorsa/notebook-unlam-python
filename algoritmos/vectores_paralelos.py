# Solución con 2 punteros al problema
# Dados dos vectores $V_A$ de largo $N$ y $V_B$ 
# de largo $M$ de números enteros, ambos ordenados 
# en orden creciente. 
# Se desea saber para cada elemento de $V_A$ 
# cuantos elementos de $V_B$ hay menores o iguales 
# a él*
# O(N+M)

def VectoresParalelos(VA : list[int],VB : list[int]) -> list[int]:
  res = [0] * len(VA)
  for i in range(len(VA)):
    if i : res[i] = res[i-1]
    while res[i] < len(VB) and VB[res[i]] <= VA[i]:
      res[i] += 1
  return res

