# heap: Estructura de datos que permite mantener un conjunto de elementos ordenados y permite insertar y extraer el mínimo en O(log n)
# heappush(h, x): Inserta x en el heap h
# heappop(h): Extrae el mínimo del heap h
# h[0] es el mínimo del heap h
# heapsort: Ordena un iterable en O(n log n)
from heapq import heappush, heappop
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]