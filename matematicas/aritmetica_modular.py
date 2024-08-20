# Realizar las operaciones con
# los enteros modulo m

def SumaMod(a, b, m):
    return (a+b)%m

def RestaMod(a, b, m):
    return ((a-b)%m+m)%m

def MultMod(a, b, m):
    return (a*b)%m