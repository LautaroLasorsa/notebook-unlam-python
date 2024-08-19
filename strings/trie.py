# Implementación de la estructura Trie
# Un Trie es un árbol donde cada nodo tiene
# un diccionario de caracteres a nodos y un contador
# de cuantas veces se ha pasado por ese nodo
# O(|S|) para todas las operaciones


T = [[0, dict()]] # (acumulador, hijos)
# Puede modificarse para guardar metadata adicional

# Agrega la cadena S al trie T
def Agregar(T : list[tuple[int,dict[str,int]]], S : str) -> int:
  nodo = 0
  for c in S:
    if c not in T[nodo][1]:
      T[nodo][1][c] = len(T)
      T.append([0, dict()])
    T[nodo][0] += 1
    nodo = T[nodo][1][c]
  T[nodo][0] += 1
  return nodo

# Borra la cadena S del trie T
def Borrar(T : list[tuple[int,dict[str,int]]], S : str) -> int: # Asume que S está representado en T
  nodo = 0
  for c in S:
    T[nodo][0] -= 1
    nodo = T[nodo][1][c]
  T[nodo][0] -= 1
  return nodo

# Busca la cadena S en el trie T
def Buscar(T : list[tuple[int,dict[str,int]]], S : str) -> int:
  nodo = 0
  for c in S:
    if c not in T[nodo][1]:
      return None
    nodo = T[nodo][1][c]
  return nodo