name= input("¿como te llamas? ")
gender= input("Cual es tu sexo (M o F)? ")

if gender =="M":
    if name.lower()< "m":
        group= "A"
    else:
        group= "B"
else:
    if name.lower()> "n":
        group= "A"
    else:
        group= "B"
print("tu grupo es "+ group)
