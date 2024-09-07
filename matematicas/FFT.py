import cmath

def next_power_of_2(x):
    return 1 << (x - 1).bit_length()

def fft(a):
    n = len(a)
    if n <= 1:
        return a
    
    even = fft(a[0::2])
    odd = fft(a[1::2])
    
    T = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    
    return [even[k] + T[k] for k in range(n // 2)] + \
           [even[k] - T[k] for k in range(n // 2)]

def ifft(a):
    n = len(a)
    a_conj = [x.conjugate() for x in a]
    y = fft(a_conj)
    return [(x.conjugate() / n) for x in y]

def convolve(x, y):
    # Determine the size needed for FFT, next power of 2
    n = next_power_of_2(len(x) + len(y) - 1)
    
    # Pad x and y with zeros to length n
    x_padded = x + [0] * (n - len(x))
    y_padded = y + [0] * (n - len(y))
    
    # Compute the FFT of both sequences
    fft_x = fft(x_padded)
    fft_y = fft(y_padded)
    
    # Point-wise multiplication of the FFTs
    fft_product = [a * b for a, b in zip(fft_x, fft_y)]
    
    # Compute the inverse FFT to get the convolution result
    result = ifft(fft_product)
    
    # Since the output may have small imaginary parts due to numerical errors, return the real part
    return [round(r.real) for r in result]
