# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
class BinaryLifting:
    def __init__(self, f, l = 0):
        self.n = len(f)
        self.l = max(l,self.n.bit_length())
        self.f = [[-1] * self.n for _ in range(self.l)]
        self.f[0] = f
        for i in range(1, self.l):
            for u in range(self.n):
                self.f[i][u] = self.f[i - 1][self.f[i - 1][u]]

    def ksig(self, u : int, k : int) -> int:
        for i in range(self.l):
            if k & (1 << i):
                u = self.f[i][u]
        return u

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        parent[0] = n
        self.bl = BinaryLifting( parent + [n])

    def getKthAncestor(self, node: int, k: int) -> int:
        r = self.bl.ksig(node,k)
        if r == self.n: return -1
        return r
