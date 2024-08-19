# Dado un string S, la función Manacher(S) devuelve 
# dos listas de enteros de longitud n, donde n es la
# longitud de S. La primera lista es impar y la segunda
# es par. La lista impar[i] es la longitud del palíndromo
# más largo con centro en S[i] y la lista par[i] es la
# longitud del palíndromo más largo con centro en el
# espacio entre S[i-1] y S[i].
# 
# Es decir, impar[i] es el máximo k tal que S[i-k:i+k]
# es un palindromo y par[i] es el máximo k tal que
# S[i-k:i+k) es un palindromo.
#  
# Recordar que un palindromo es una cadena que se lee
# igual de izquierda a derecha que de derecha a izquierda.
#
# O(n).


def Manacher(S : str) -> tuple[list[int],list[int]]:
  n = len(S)
  par, impar = [0]*n, [0]*n
  l, r = 0, -1
  for i in range(n):
    k = 1 if i>r else min(impar[l+r-i],r-i)
    while i+k<n and i-k>=0 and S[i+k]==S[i-k]:
      k+=1
    k -= 1
    impar[i] = k
    if i+k>r: l, r = i-k, i+k

  l,r = 0, -1
  for i in range(n):
    k = 1 if i>r else min(par[l+r-i+1],r-i+1)+1
    while i+k<=n and i-k>=0 and S[i+k-1]==S[i-k]:
      k+=1
    k -= 1
    par[i] = k
    if i+k-1>r: l, r = i-k, i+k-1
  return impar, par

#Ejemplo
#S = "aabbaacaabbaa"
#impar, par = Manacher(S)
#print(impar)
#[0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0]
#print(par)
#[0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 3, 0, 1]