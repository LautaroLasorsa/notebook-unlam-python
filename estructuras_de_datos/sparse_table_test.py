# https://cses.fi/problemset/task/1647

def operation(a, b):
    return a + b

def next_p2(n: int) -> int:
    return 1 << (n - 1).bit_length()

# Función que recibe un vector y construye su Sparse Table
# O(NlogN)
def st_build(v ) :
    n = len(v)
    k = n.bit_length()
    st = [[0] * k for _ in range(n)]
    for i in range(n):
        st[i][0] = v[i]
    for j in range(1, k):
        for i in range(n - (1 << j) + 1):
            st[i][j] = operation(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
    return st

# O(1): Usar si la operación es idempotente (ej: mínimo, máximo, and, or)
def st_query(st , l : int, r : int) -> any:
    j = r - l
    k = j.bit_length() - 1
    return operation(st[l][k], st[r - (1 << k)][k])

# O(log(n)): Usar si la operación no es idempotente (ej: suma, producto)
#def st_query(st : list[list[any]], l : int, r : int) -> any:
#    res = None
#    for k in range(len(st[0]) - 1, -1, -1):
#        if l + (1 << k) <= r:
#            if res == None: res = st[l][k]
#            else: operation(st[l][k], st_query(st, l + (1 << k), r))
#            l += 1 << k
#    return res

n, q = map(int,input().split())
xs = list(map(int, input().split()))
st = st_build(xs)
for _ in range(q):
    l, r = map(int,input().split())
    l -= 1
    print(st_query(st,l,r))