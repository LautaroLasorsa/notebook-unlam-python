# Calcula el Divisor Común Mayor de a y b
# O(log(min(a,b)))
# Notar que es una operación:
# - Asociativa
# - Conmutativa
# - Tiene elemento neutro: 0
# - No tiene inverso
# - Idempotente (gcd(a,a) = a)

def gcd(a : int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a