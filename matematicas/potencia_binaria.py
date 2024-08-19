# Calcula base^e modulo mod en O(log(e))
# Para numeros enteros se puede reemplazar
# por la ya implementada math.pow(base,e,mod)

def Potencia(base, e, mod):
    res = 1 # Elemento neutro de la multiplicación
    while e > 0:
        if e%2 == 1: # Encuentro los 1 de la representación binaria del exponente
            res = MultMod(res, base, mod) # Acumulo el resultado
        base = MultMod(base, base, mod) # Siguiente potencia de base
        e = e//2 # Siguiente dígito de la representación binaria
    return res
# Si el modulo es primo y a != 0 (mod) entonces
# a^(mod-1) = 1 (mod)
# a^(mod-2) = a^(-1) (mod)
def inv(a,mod):
    return Potencia(a,mod-2,mod)