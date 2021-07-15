from math import radians, sin, cos, tan

opuesto = ang = 0.0
hipo = ady = 0.0
radianes = 0.0

opuesto = float(input("Opuesto: "))
ang = float(input("Angulo: "))


radianes = radians(ang)

hipo = opuesto / cos(radianes)
ady = opuesto *tan(radianes)

print("\nSalida Resultados")
print("Hipotenusa: ",hipo)
print("Adyacente: ", ady)
      
                   
