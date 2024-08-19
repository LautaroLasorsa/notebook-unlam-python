# Calcula el array de bordes de un string
# Un borde es un substring propio que es
# tanto prefijo como sufijo
# bordes[i] = k => s[:k) es el mayor borde de s[:i)
# Complejidad: O(n)

# Notar que podemos obtener las apariciones de un
# string T en un string S calculando 
# bordes(T + "#" + S) y contando las apariciones
# de T en los bordes

def bordes(S : str) -> list[int]:
  bordes = [0] * len(S)
  for i in range(1, len(S)): 
    # Invariante: bordes[0:i) ya computados
    j = bordes[i - 1]
    while j > 0 and S[i] != S[j]:
      j = bordes[j - 1]
    if S[i] == S[j]:
      j += 1
    bordes[i] = j
  return [0] + bordes 
  # para que coincida con la convención

# bordes("abacaba")
# [0, 0, 1, 0, 1, 2, 3, 0]