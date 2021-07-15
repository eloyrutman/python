from math import sqrt , pi

l = r = vc = 0.0
ve = 0.0
vv = 0.0

l = float(input("Longitud del Cubo: "))

r = l/2
vc = l**3
ve = 4/3*pi*r**3
vv = vc-ve

print ("Volumen vacio es: ", vv)
print ("Fin del programa")

