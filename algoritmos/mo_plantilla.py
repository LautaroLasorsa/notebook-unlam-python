# Plantilla para aplicar el algoritmo de Mo a cualquier problema
# Requisitos
# - Se realizán consultas de forma asincronica
# - No hay actualizaciones
# - La función AgregarElemento debe ser implementada
# - La función EliminarElemento debe ser implementada
# - La variable neutro debe ser definida
# CUIDADO: Si la operación no es conmutativa, deben implementar
# versiones por izquierda y derecha de 
# AgregarElemento y EliminarElemento
# para evitar errores
# Complejidad: O((N+Q) * sqrt(N) * O(Agregar/Eliminar Elemento))
# En Python es probable que de TLE, en C++ no debería
# Formato del input: [l,r)

def AgregarElemento(actual, elemento):
    # Recomputa la respuesta al agregar un nuevo elemento
    # ejemplo : return actual + elemento

def EliminarElemento(actual, elemento):
    # Recomputa la respuesta al eliminar un elemento
    # ejemplo : return actual - elemento

def Mo(V : list[int], L : list[int], R:list[int]) -> list[int]:
  N, Q = len(V), len(R)
  queries = [(L[i], R[i], i) for i in range(Q)]
  BASE = int(N**0.5)
  vec_res = [0] * Q
  queries.sort(key=lambda x: (x[0]//BASE, x[1]))
  i, j, res = 0, 0, neutro # Cambiar neutro por el valor neutro de la operación
  for l, r, idx in queries:
    while i < l:
        res = EliminarElemento(res, V[i])
        i += 1
    while i > l:
        i -= 1
        res = AgregarElemento(res, V[i])
    while j < r:
        res = AgregarElemento(res, V[j])
        j += 1
    while j > r:
        j -= 1
        res = EliminarElemento(res, V[j])
    vec_res[idx] = res
  return vec_res