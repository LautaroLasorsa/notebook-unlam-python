# https://cses.fi/problemset/task/1648
# https://cses.fi/problemset/task/1649

SUMA = False 

class SegmentTree:
    if SUMA:
        def Op(self, a, b): 
            return a + b
        neutro = 0
    else:
        def Op(self, a, b): 
            return min(a, b)
        neutro = float('inf')
    
    # Ejemplo de posible operacion
    #def Op(self, a, b): 
    #    return a + b if SUMA else min(a, b)
    # Ejemplo del neutro de la operación
    #neutro = 0 if SUMA else float('inf')

    def __init__(self, V): 
        # La función __init__ nos permite crear un nuevo elemento de la clase
        n = len(V)
        self.largo = 1 
        # El largo que será representado por el árbol de segmentos
        while self.largo < n:
            self.largo *= 2 
            # Tiene que ser mayor o igual a n
        self.st = [self.neutro for i in range(2 * self.largo)] 
        # Crea el árbol inicialmente con el neutro
        for i in range(n):
            self.st[self.largo + i] = V[i] # Inicializa las hojas del vector
        for i in range(self.largo - 1, 0, -1):
            self.st[i] = self.Op(self.st[i * 2], self.st[i * 2 + 1]) 
            # Inicializa los nodos internos del vector

    def Consulta(self, l, r):
        # Consultas iterativas para mejor performance
        # Puede ser la diferencia entre AC y TLE
        l += self.largo
        r += self.largo
        lres = self.neutro
        rres = self.neutro
        while l <= r:
            if l % 2 == 1:
                lres = self.Op(lres, self.st[l])
                l += 1
            if r % 2 == 0:
                rres = self.Op(self.st[r], rres)
                r -= 1
            l //= 2
            r //= 2
        return self.Op(lres, rres)

    def Actualizar(self, i, v):
        i += self.largo 
        # La posición i en el vector es i + largo en el árbol
        self.st[i] = v # Actualiza el valor en la posición i
        i //= 2 # Accedo al padre de i
        while i >= 1:
            # print(f"Actualizo el nodo {i} accediendo a sus hijos {i*2} e {i*2+1}")
            self.st[i] = self.Op(self.st[i * 2], self.st[i * 2 + 1]) 
            #Actualizo el valor del nodo
            i //= 2 # Accedo al padre de i

n, q = map(int, input().split())
V = list(map(int, input().split()))
st = SegmentTree(V)
for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        st.Actualizar(b-1, c)
    else:
        print(st.Consulta(b-1, c-1))