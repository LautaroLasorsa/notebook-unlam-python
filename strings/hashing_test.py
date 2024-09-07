# https://cses.fi/problemset/result/10439364/
# TLE, sin ningún WA 
p = 2**61 - 1
B = [34324123048] #, 138478293]

def suma(a  , b  )  :
    sum = [0] * len(a)
    for i in range(len(a)):
        sum[i] = (a[i] + b[i]) % p
    return sum

def mult(a , b  )  :
    mult = [0] * len(a)
    for i in range(len(a)):
        mult[i] = (a[i] * b[i]) % p
    return mult

def resta(a , b )  :
    res = [0] * len(a)
    for i in range(len(a)):
        res[i] = (a[i] - b[i]) % p
    return res

def of(a : int):
    h = [0] * len(B)
    for i in range(len(B)):
        h[i] = a % p
    return h

def invof(a ):
  g = of(1)
  e = p-2
  while e:
    if e & 1:
      g = mult(g, a)
    a = mult(a, a)
    e //= 2
  return g

_po = [of(1)]
def po(n : int)  :
    while len(_po) <= n:
        _po.append(mult(_po[-1], B))
    return _po[n]

inv = invof(B)
_ipo = [of(1)]
def invpo(n : int)  :
    while len(_ipo) <= n:
        _ipo.append(mult(_ipo[-1], inv))
    return _ipo[n]

def getHash(s)  :
    if isinstance(s, str):
        s = [ord(c) for c in s]
    h = [of(0)]
    for i, c in enumerate(s):
        h.append(suma(h[-1], mult(po(i), of(c))))
    # Usamos el H1 definido antes
    # h[l] es el hash en [0,l)
    return h

def getSubHash(h, l : int, r : int)  :
    return mult(resta(h[r],h[l]),invpo(l))
    # Obtengo el hash de [l,r)

s = input()
pat = input()

hs = getHash(s)
hp = getHash(pat)[-1]
res = 0
for i in range(len(s) - len(pat) + 1):
    if hp == getSubHash(hs, i, i + len(pat)):
        res += 1
print(res)