# https://cses.fi/problemset/task/2107
def bordes(S):
  bordes = [0] * len(S)
  for i in range(1, len(S)): 
    # Invariante: bordes[0:i) ya computados
    j = bordes[i - 1]
    while j > 0 and S[i] != S[j]:
      j = bordes[j - 1]
    if S[i] == S[j]:
      j += 1
    bordes[i] = j
  return [0] + bordes 

def array_z(S):
  l, r, n = 0, 0, len(S)
  z = [0]*n 
  # z[i] = max k: s[0,k) == s[i,i+k)
  for i in range(1, n): 
    # Invariante: s[0,r-l) == s[l,r)
    if i <= r:
      z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < n and S[z[i]] == S[i + z[i]]:
      z[i] += 1
    if i + z[i] - 1 > r:
      l, r = i, i + z[i] - 1
  # No coincide con la convención
  # z[0] = len(S)
  return z

s = input()
print(" ".join(map(str,array_z(s))))
print(" ".join(map(str,bordes(s)[1:])))
