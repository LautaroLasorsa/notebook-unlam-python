# Dado un N y un modulo mod, computa en O(N)
# los factoriales y sus inversos modulo mod
# hasta N inclusive
# idea: https://codeforces.com/blog/entry/83075
# O(N)
def precomputo(N : int, mod : int):
    fact = [1] * (N+1)
    inv = [1] * (N+1)
    inv_fact = [1] * (N+1)
    for i in range(2,N+1):
        fact[i] = (fact[i-1] * i) % mod
        inv[i] = (mod - (mod // i) * inv[mod % i]) % mod
        inv_fact[i] = (inv_fact[i-1] * inv[i]) % mod
    # fact[i] = factorial de i
    # inv[i] = inverso de i
    # inv_fact[i] = inverso del factorial de i
    return fact, inv, inv_fact