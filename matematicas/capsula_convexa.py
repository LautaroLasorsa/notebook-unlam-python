# Calcula la Capsula Convexa de un conjunto
# de puntos en el plano
# La capsula convexa es el mínimo poligono
# convexo que contiene todos los puntos
# Es mínima en, al menos, los siguientes sentidos
# - Minima area
# - Minimo perimetro
# - Está incluida en cualquier otro poligono
#   convexo que contenga todos los puntos

# Esta es una implementación distinta a la vista en clase
# porque es mucho más eficiente y soporta mejor tener 3 o más 
# puntos colineales

# Complejidad: O(n log n)
# Necesita tener implementadas las funciones de punto.py

def angulo(a, b, c):
    return (a[0] * (b[1] - c[1]) + 
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))


def CapsulaConvexa(puntos):
    puntos = puntos.copy()
    if len(puntos) <= 3:
        return puntos
    puntos.sort()
    cap = []
    # En la comparativa poner >0 para incluir puntos alineados
    # Poner >=0 para excluir puntos alineados
    for p in puntos:
        while len(cap)>1 and angulo(cap[-2],cap[-1],p)>0:
            cap.pop()
        cap.append(p)
    cap.pop()
    puntos.reverse()
    for p in puntos:
        while len(cap)>1 and angulo(cap[-2],cap[-1],p)>0:
            cap.pop()
        cap.append(p)
    return cap
    
# usar cap, puntos = CapsulaConvexa(ps) para obtener la capsula convexa 
# y los puntos ordenados.
