import cmath

def fft_iterative(a):
    n = len(a)
    levels = n.bit_length() - 1
    
    # Bit-reversed addressing permutation
    a = [a[int(f'{i:0{levels}b}'[::-1], 2)] for i in range(n)]
    
    # Cooley-Tukey FFT
    size = 2
    while size <= n:
        halfsize = size // 2
        table_step = n // size
        for i in range(0, n, size):
            for j in range(halfsize):
                k = j * table_step
                twiddle = cmath.exp(-2j * cmath.pi * k / n) * a[i + j + halfsize]
                a[i + j + halfsize] = a[i + j] - twiddle
                a[i + j] = a[i + j] + twiddle
        size *= 2
    
    return a

def ifft_iterative(a):
    n = len(a)
    a_conj = [x.conjugate() for x in a]
    y = fft_iterative(a_conj)
    return [(x.conjugate() / n) for x in y]

def convolve_iterative(x, y):
    n = next_power_of_2(len(x) + len(y) - 1)
    
    x_padded = x + [0] * (n - len(x))
    y_padded = y + [0] * (n - len(y))
    
    fft_x = fft_iterative(x_padded)
    fft_y = fft_iterative(y_padded)
    
    fft_product = [a * b for a, b in zip(fft_x, fft_y)]
    
    result = ifft_iterative(fft_product)
    
    return [round(r.real) for r in result]

def next_power_of_2(x):
    return 1 << (x - 1).bit_length()