# Funciones para trabajar con poligonos convexos

# Dados los puntos de un poligono convexo en orden anti-horario
# retorna el area del poligono. (Si están en sentido 
# horario el area es negativa)
def Area_Poligono(puntos): # se asumen ordenados
  p = puntos[0]
  return sum(producto_cruz(resta_punto(puntos[i],p),
        resta_punto(puntos[(i+1)%len(puntos)],p)) 
        for i in range(len(puntos)))/2

# Calcula si un punto está dentro de un poligono convexo
# Asume que los puntos están ordenados en sentido horario
# o anti-horario
# O(N)
def PuntoEnPoligono(p,puntos):
  for i in range(len(puntos)):
    p_i = puntos[i]
    p_ip1 = puntos[(i+1)%len(puntos)]
    area = producto_cruz(resta_punto(p_i,p),resta_punto(p_ip1,p))
    if area<0:
      return False
  return True