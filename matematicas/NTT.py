def ntt(a, n, p, g):
    # Aplica la Transformada Número Teórico (NTT) a la secuencia a
    result = a[:]
    for length in range(1, n, 2):
        w_n = pow(g, (p - 1) // (2 * length), p)
        w = 1
        for start in range(0, n, 2 * length):
            for i in range(length):
                u = result[start + i]
                v = (result[start + i + length] * w) % p
                result[start + i] = (u + v) % p
                result[start + i + length] = (u - v) % p
            w = (w * w_n) % p
    return result

def intt(a, n, p, g):
    # Aplica la Transformada Número Teórico Inversa (INTT)
    n_inv = pow(n, p - 2, p)  # Inversa de n módulo p
    g_inv = pow(g, p - 2, p)  # Inversa de g módulo p
    
    result = ntt(a, n, p, g_inv)
    return [(x * n_inv) % p for x in result]

def next_power_of_2(x):
    # Calcula la siguiente potencia de 2 mayor o igual a x
    return 1 << (x - 1).bit_length()

def convolve_ntt(a, b, p, g):
    # Realiza la convolución usando NTT sin asumir que el tamaño es potencia de 2
    n = len(a) + len(b) - 1
    n_padded = next_power_of_2(n)
    
    # Rellena las secuencias con ceros hasta la siguiente potencia de 2
    a_padded = a + [0] * (n_padded - len(a))
    b_padded = b + [0] * (n_padded - len(b))
    
    # Aplica NTT a ambas secuencias
    ntt_a = ntt(a_padded, n_padded, p, g)
    ntt_b = ntt(b_padded, n_padded, p, g)
    
    # Multiplicación punto a punto
    ntt_c = [(x * y) % p for x, y in zip(ntt_a, ntt_b)]
    
    # Aplica la NTT inversa
    result = intt(ntt_c, n_padded, p, g)
    
    # Trunca al tamaño real del resultado de la convolución
    return result[:n]

# Ejemplo de uso
# a = [1, 2, 3]
# b = [4, 5, 6]
# p = 998244353  # Un número primo
# g = 3          # Una raíz primitiva módulo 998244353

#result = convolve_ntt(a, b, p, g)
