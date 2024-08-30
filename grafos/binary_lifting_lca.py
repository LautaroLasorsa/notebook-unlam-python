# Estructura de datos que almacena el Binary
# Lifting de un árbol

class BinaryLifting:
    
    def __init__(self, g : list[list[int]], \
                 raiz : int = 0, l : int = 0):
        self.n = len(g)
        self.l = max(l,self.n.bit_length())
        self.padres = [[-1] * self.n for _ in range(self.l)]
        self.depth = [0] * self.n
        self.padres[0][raiz] = raiz
        pila = [raiz]
        while pila:
            u = pila[-1]
            pila.pop()
            for v in g[u]:
                if self.padres[0][v] == -1:
                    self.padres[0][v] = u
                    self.depth[v] = self.depth[u] + 1
                    pila.append(v)
        for i in range(1, self.l):
            for u in range(self.n):
                self.padres[i][u] =\
                self.padres[i - 1][self.padres[i - 1][u]]
    
    def kancestro(self, u : int, k : int) -> int:
        for i in range(self.l):
            if k & (1 << i):
                u = self.padres[i][u]
        return u
    
    def lca(self, u : int, v : int) -> int:
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        v = self.kancestro(v, self.depth[v] - self.depth[u])
        if u == v:
            return u
        for i in range(self.l - 1, -1, -1):
            if self.padres[i][u] != self.padres[i][v]:
                u = self.padres[i][u]
                v = self.padres[i][v]
        return self.padres[0][u]

    def add_hijo(self, p : int) -> None:
        v = len(self.padres)
        self.padres.append([p] + [-1] * (self.l - 1))
        self.depth.append(self.depth[p] + 1)
        for i in range(1, self.l):
            self.padres[i][v] = \
            self.padres[i - 1][self.padres[i - 1][v]]
