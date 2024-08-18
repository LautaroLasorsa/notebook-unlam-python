# Plantilla para aplicar el algoritmo de Mo a cualquier problema
# Requisitos
# - Se realizán consultas de forma asincronica
# - No hay actualizaciones
# - La función AgregarElemento debe ser implementada
# - La función EliminarElemento debe ser implementada
# - La variable neutro debe ser definida
# CUIDADO: Si la operación no es conmutativa, deben implementar
# versiones por izquierda y derecha de AgregarElemento y EliminarElemento
# para evitar errores
# Complejidad: O((N+Q) * sqrt(N) * O(Agregar/Eliminar Elemento))
# Formato del input : [l,r) 

# https://cses.fi/problemset/task/1646

def AgregarElemento(actual, elemento):
    # Recomputa la respuesta al agregar un nuevo elemento
    # ejemplo : return actual + elemento
    return actual + elemento
def EliminarElemento(actual, elemento):
    # Recomputa la respuesta al eliminar un elemento
    # ejemplo : return actual - elemento
    return actual - elemento

neutro = 0

def Mo(V , L , R) :
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
    # print(f"l: {l}, r: {r}, idx: {idx}, res: {res}, {V[l:r]=}")
    vec_res[idx] = res
  return vec_res

n, q = map(int, input().split())
V = list(map(int, input().split()))
L, R = [], []
for i in range(q):
    l, r = map(int, input().split())
    L.append(l-1)
    R.append(r)

res = Mo(V, L, R)
print("\n".join(map(str, res)))

# Previsiblemente, da TLE en Python