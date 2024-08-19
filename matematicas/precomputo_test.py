import precomputo_factoriales_e_inversos

N = 10_000_000
mod = 10**9 + 7
fact, inv, inv_fact = precomputo_factoriales_e_inversos.precomputo(N,mod)
for i in range(N+1):
    if fact[i] * inv_fact[i] % mod != 1:
        print(i)
        print(fact[i],inv_fact[i])
    assert (fact[i] * inv_fact[i]) % mod == 1