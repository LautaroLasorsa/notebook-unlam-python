# Dado un grafo funcional
# Permite calcular consultas de
# realizar k pasos desde un nodo u
# en O(logN). Notar que si en un árbol
# cada nodo apunta a su padre tenemos un grafo
# funcional.
# O(NlogN) en la inicialización
# O(logN) por consulta

class BinaryLifting:
    def __init__(self, f : list[int]):
        self.n = len(f)
        self.l = self.n.bit_length()
        self.f = [[-1] * self.n for _ in range(self.l)]
        self.f[0] = f
        for i in range(1, self.l):
            for u in range(self.n):
                self.f[i][u] = \
                self.f[i - 1][self.f[i - 1][u]]
    # Obtiene f^k(u)
    def ksig(self, u : int, k : int) -> int:
        for i in range(self.l):
            if k & (1 << i):
                u = self.f[i][u]
        return u
