# 
# def angulo(p1,p2,p3):
#    return ((p1[0]-p2[0])*(p3[1]-p2[1])-(p1[1]-p2[1])*(p3[0]-p2[0]))
    #return producto_cruz(resta_puntos(p1,p2),resta_puntos(p3,p2))

def angulo(a, b, c):
    return (a[0] * (b[1] - c[1]) + 
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))


def CapsulaConvexa(puntos):
    puntos = puntos.copy()
    if len(puntos) <= 3:
        return puntos
    puntos.sort()
    cap = []
    for p in puntos:
        while len(cap)>1 and angulo(cap[-2],cap[-1],p)>0:
            cap.pop()
        cap.append(p)
    cap.pop()
    puntos.reverse()
    for p in puntos:
        while len(cap)>1 and angulo(cap[-2],cap[-1],p)>0:
            cap.pop()
        cap.append(p)
    return cap
    
# usar cap, puntos, _ = CapsulaConvexa(ps) para obtener la capsula convexa 
# y los puntos ordenados.

n = int(input())
ps = [None] * n
for i in range(n):
    x, y = map(int, input().split())
    ps[i] = (x, y)

# ps = [list(map(int,input().split())) for _ in range(n)]
cap = CapsulaConvexa(ps)
print(len(cap)-1)
# print(cap)
print('\n'.join(str(x[0]) + " " +str(x[1]) for x in cap[:-1]))