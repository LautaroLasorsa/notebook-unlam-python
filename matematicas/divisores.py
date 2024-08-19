# Calcula los divisores de cada número hasta N
# O(Nlog(N))

def Divisores(N:int) -> list[list[int]]:
    divisores = [ [] for _ in range(N + 1) ]
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            divisores[j].append(i)
    return divisores