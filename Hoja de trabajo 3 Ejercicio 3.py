g=int(input("Ingresa un numero positivo mayor que 2: "))

i = 2
while g % i !=0:
    i += 1
if i==g:
    print(str(g)+ " es primo")
else:
    print(str(g)+ " no es primo")
