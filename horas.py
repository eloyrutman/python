hi = 0; mi = 0
hs = 0; ms = 0
dur = 0; tmi = 0
tms = 0; hd = 0
md = 0; costo = 0


hi = int(input("Hora de Inicio: "))
mi = int(input("Minuto de Inicio: "))
hs = int(input("Hora de Fin: "))
ms = int(input("Minuto de Fin: "))

tmi = hi * 60 + mi
tms = hs * 60 + ms
dur = tms-tmi
hd = dur // 60
md = dur % 60
costo = dur * 1.25

print("Duró: ",hd ,"horas y ", md , "minutos")
print("Costó: ",costo, "Bs")


