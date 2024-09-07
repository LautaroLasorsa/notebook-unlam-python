p = 2**61 - 1
B = [34324123048, 138478293]

def suma(a : list[int], b : list[int]) -> list[int]:
    return [(x + y) % p for x, y in zip(a, b)]

def mult(a : list[int], b : list[int]) -> list[int]:
    return [(x * y) % p for x, y in zip(a, b)]
  
def resta(a : list[int], b : list[int]) -> list[int]:
    return [(x - y) % p for x, y in zip(a, b)]

def of(a : int):
    return [a % p for _ in range(len(B))]

def invof(a : list[int]):
  g = of(1)
  e = p-2
  while e:
    if e & 1:
      g = mult(g, a)
    a = mult(a, a)
    e //= 2
  return g

_po = [of(1)]
def po(n : int) -> list[int]:
    while len(_po) <= n:
        _po.append(mult(_po[-1], B))
    return _po[n]

inv = invof(B)
_ipo = [of(1)]
def invpo(n : int) -> list[int]:
    while len(_ipo) <= n:
        _ipo.append(mult(_ipo[-1], inv))
    return _ipo[n]

def getHash(s : str | list[int]) -> list[int]:
    if isinstance(s, str):
        s = [ord(c) for c in s]
    h = [of(0)]
    for i, c in enumerate(s):
        h.append(suma(h[-1], mult(po(i), of(c))))
    # Usamos el H1 definido antes
    # h[l] es el hash en [0,l)
    return h

def getSubHash(h : list[int], l : int, r : int) -> list[int]:
    return mult(resta(h[r],h[l]),invpo(l))
    # Obtengo el hash de [l,r)
