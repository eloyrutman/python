from math import radians, sin, cos

hipo = ang = 0.0
cateto1 = cateto2 = 0.0
radianes = 0.0

hipo = float(input("Hipotenusa: "))
ang = float(input("Angulo: "))


radianes = radians(ang)

cateto1 = hipo * sin(radianes)
cateto2 = hipo * cos(radianes)

print("\nSalida Resultados")
print("Cateto 1: ",cateto1)
print("Cateto 2: ", cateto2)
      
                   
