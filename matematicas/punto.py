# En esta archivo están las funciones para trabajar
# con puntos/vectores. 
# Un vector en R^n  es una lista de n números reales
# Un punto en R^n es un vector en R^n
# Ej: Un punto en R^2 es una lista de 2 números reales
# Ej: Un punto en R^3 es una lista de 3 números reales


# Calcular la norma (tamaño) de un vector en R^n
def norma2(p : list[float]) -> float: 
# Retorna el cuadrado de la norma de un vector
    return sum([x**2 for x in p]) 
# Recordar que sum nos devuelve la suma de todos los elementos de un iterable

def norma(p : list[float]) -> float: 
# Retorna la norma de un vector
    return norma2(p)**0.5

# Operar con puntos/vectores

def suma_puntos(p1 : list[float], p2 : list[float]) -> list[float]: 
    # Retorna la suma de dos puntos
    return [p1[i] + p2[i] for i in range(len(p1))]

def producto_por_escalar(p : list[float], k : float) -> list[float]: 
    # Retorna el producto de un punto por un escalar
    return [k * x for x in p]

def resta_puntos(p1 : list[float], p2 : list[float]) -> list[float]: 
    # Retorna la resta de dos puntos
    return [p1[i] - p2[i] for i in range(len(p1))] 
# Recordar que range(n) nos devuelve un iterable con los números del 0 al n-1

# Calcular la distancia entre 2 puntos
def distancia(p1 : list[float], p2 : list[float]) -> float: 
    # Retorna la distancia entre dos puntos
    return norma(resta_puntos(p1, p2))

def distancia2(p1 : list[float], p2 : list[float]) -> float: 
    # Retorna el cuadrado de la distancia entre dos puntos
    return norma2(resta_puntos(p1, p2))

# Calcular el producto punto entre dos vectores
def producto_punto(p1 : list[float], p2 : list[float]) -> float: 
    # Retorna el producto punto entre dos puntos
    return sum([p1[i] * p2[i] for i in range(len(p1))])

# Calcular el producto cruz entre dos vectores en R^2
def producto_cruz(p1,p2):
    return p1[0]*p2[1]-p1[1]*p2[0]

# Calcular el producto cruz entre dos vectores en R^3
def producto_cruz3(p1,p2):
    return [p1[1]*p2[2]-p1[2]*p2[1],
            p1[2]*p2[0]-p1[0]*p2[2],
            p1[0]*p2[1]-p1[1]*p2[0]]