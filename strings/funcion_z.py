# Calcula la función z de un string
# La función z de un string S es un arreglo
# de longitud n tal que z[i] es la longitud
# del string más largo que comienza en S[i]
# que es prefijo de S
# Es decir, el Prefijo Común Mayor entre
# S y S[i:]
# Se puede utilizar para encontrar todas las
# ocurrencias de un string T en S
# Calculando z(T + "#" + S) y buscando los
# valores de z iguales a la longitud de T
# Complejidad: O(n)

def array_z(S : str) -> list[int]:
  l, r, n = 0, 0, len(S)
  z = [0]*n 
  # z[i] = max k: s[0,k) == s[i,i+k)
  for i in range(1, n): 
    # Invariante: s[0,r-l) == s[l,r)
    if i <= r:
      z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < n and S[z[i]] == S[i + z[i]]:
      z[i] += 1
    if i + z[i] - 1 > r:
      l, r = i, i + z[i] - 1
  z[0] = len(S) 
  # Por convención puede ser z[0] = 0
  return z

# array_z("xaxbxxax")
# [8, 0, 1, 0, 1, 3, 0, 1]