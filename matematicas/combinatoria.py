# Factorial: n! = n * (n-1) * (n-2) * ... * 1
# Cantidad de formas de ordenar n elementos
# distintos en una fila
# Necesario definir mod

# Usamos memorización para evitar calculos innecesarios
_factorial = [1]
def Factorial(n : int, mod : int) -> int:
    while len(_factorial) <= n:
        _factorial.append(MultMod(_factorial[-1],len(_factorial),mod))
    return _factorial[n]


# Combinatoria: nCr = n! / (r! * (n-r)!)
# Cantidad de subconjuntos de tamaño k 
# de un conjunto de tamaño n
# Necesario definir mod

def Combinatoria(n : int, r : int, mod : int) -> int:
    if r > n: return 0
    return MultMod(
        MultMod(Factorial(n),inv(Factorial(r),mod),mod),
        inv(Factorial(n-r),mod),mod)

# Variaciones con Repetición
# Cantidad de formas de elegir r elementos
# de un conjunto de n elementos con repetición
# Necesario definir mod

def VR(n : int, r : int, mod : int) -> int:
    return PotenciaMod(n, r, mod)

# Variaciones sin repetición
# Cantidad de formas de elegir r elementos
# de un conjunto de n elementos sin repetición
# Necesario definir mod

def V(n : int, r : int, mod : int) -> int:
  return MultMod(Factorial(n),inv(Factorial(n-r),mod),mod)

# Permutaciones con repetición
# Cantidad de formas de ordenar un multiconjunto
# con n1, n2, ..., n_k repeticiones de los elementos
# 1, 2, ..., k

def P(ns : list[int], mod : int) -> int:
    n = sum(ns)
    res = Factorial(n,mod)
    for a in ns:
        res = MultMod(res,inv(Factorial(a,mod),mod),mod)
    return res

# Recordar:
# Si tengo X con OX ordenes validos e Y con OY 
# ordenes validos, puedo unirlos y si no hay
# restrcciones entre sus elementos 
# (X U Y) tiene C(|X|+|Y|,|X|) * OX * OY ordenes
# validos