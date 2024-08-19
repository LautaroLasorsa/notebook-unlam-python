# Obtiene todos los divisores de un número N
# Complejidad: O(sqrt(N))

def DivisoresInd(N :int) -> list[int]:
    divisores = []
    for i in range(1, N):
        if i * i > N: # Es mejor que buscar calcular la raiz cuadrada de antes
            break
        if N % i == 0: # Si i es divisor
            divisores.append(i) # Lo añadimos
            if i != N // i: # Si i no es la raiz cuadrada
                divisores.append(N // i) # Añadimos el otro divisor
    return divisores