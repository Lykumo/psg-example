# Convertir a cuantos días, horas, minutos y segundos corresponde la siguiente cantidad de segundos: 288325
segundos = 288325
dias = segundos // 86400
sobrante1 = segundos % 86400
horas = sobrante1 // 3600
sobrante2 = sobrante1 % 3600
minutos = sobrante2 // 60
sobrante3 = sobrante2 % 60

print ("288325 segundos son:")
print ("Días")
print (dias)
print ("Horas")
print (horas)
print ("Minutos")
print (minutos)
print ("Segundos")
print (sobrante3)