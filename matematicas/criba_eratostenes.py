# Calcula la criba de Eratóstenes hasta N
# Para cada número 0 <= i <= N, criba[i] es True
# si i es primo, False en caso contrario
# O(Nlog(log(N))

def Eratostenes(N:int) -> list[bool]:
    criba = [False] * 2 + [True] * (N - 1) 
    # El 0 y el 1 sabemos que no lo son
    for p in range(2, N + 1): 
        # Iteramos los números de 2 a N
        if criba[p]: # Si p es primo
            for i in range(p * p, N + 1, p): 
            # Recorremos de a saltos de longitud p
                criba[i] = False
    return criba

# para listar primos
primos = Eratostenes(N)
print(list(filter(lambda x: primos[x], range(N+1))))

