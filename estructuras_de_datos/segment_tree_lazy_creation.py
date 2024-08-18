# Árbol de Segmentos
# Se inicializa con un entero n que índica el tamaño del
# dominio. Inicialmente todos los valores son el neutro
# de la operación
# Permite trabajar con un dominio arbitrariamente grande
# Permite aplicar una operacion op() asociativa a
# un rango [l,r] de V.
# Se deben definir:
# * La operación op(a, b)
# * El valor neutro de la operación
# Complejidad (llamados a op):
# * Construcción: O(n)
# * Consulta: O(log(n))
# * Actualización: O(log(n))

class SegmentTreeLazy:
    # Ejemplo de posible operacion
    def Op(self, a, b): 
        return a + b
    # Ejemplo del neutro de la operación
    neutro = 0

    def __init__(self, n): 
        # La función __init__ nos permite crear un nuevo elemento de la clase
        self.largo = 1
        while self.largo < n:
            self.largo *= 2
        self.st = dict()

    def Consulta(self, lq, rq, nodo = 1, l = 0, r = - 1):
        if r == -1: r = self.largo-1 
        # Si r no fue dado, se asume que es el largo del árbol - 1
        if l > rq or r < lq or nodo not in self.st: 
            # Si el intervalo [l, r] está completamente fuera de [lq, rq]
            return self.neutro
        if lq <= l and r <= rq: 
            # Si el intervalo [l, r] está completamente dentro de [lq, rq]
            return self.st[nodo]
        m = (l + r) // 2
        # Si el intervalo [l, r] está parcialmente dentro de [lq, rq]
        return self.Op(self.Consulta(lq, rq, nodo * 2, l, m), self.Consulta(lq, rq, nodo * 2 + 1, m+1, r))

    def Actualizar(self, i, v):
        i += self.largo # La posición i en el vector es i + largo en el árbol
        self.st[i] = v # Actualiza el valor en la posición i
        i //= 2 # Accedo al padre de i
        while i >= 1:
            self.st[i] = self.Op(self.st.get(i*2,self.neutro), self.st.get(i * 2 + 1,self.neutro)) 
            #Actualizo el valor del nodo
            i //= 2 
            # Accedo al padre de i