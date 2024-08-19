# https://cses.fi/problemset/task/1111

def Manacher(S):
  n = len(S)
  par, impar = [0]*n, [0]*n
  l, r = 0, -1
  for i in range(n):
    k = 1 if i>r else min(impar[l+r-i],r-i)
    while i+k<n and i-k>=0 and S[i+k]==S[i-k]:
      k+=1
    k -= 1
    impar[i] = k
    if i+k>r: l, r = i-k, i+k

  l,r = 0, -1
  for i in range(n):
    k = 1 if i>r else min(par[l+r-i+1],r-i+1)+1
    while i+k<=n and i-k>=0 and S[i+k-1]==S[i-k]:
      k+=1
    k -= 1
    par[i] = k
    if i+k-1>r: l, r = i-k, i+k-1
  return impar, par

s = input()
impar, par = Manacher(s)
l,r = 0,0
for i in range(len(s)):
    if 2 * impar[i]+1 > r-l:
        l = i - impar[i]
        r = i + impar[i]+1
    if 2 * par[i] > r-l:
        l = i - par[i]
        r = i + par[i]
print(s[l:r])