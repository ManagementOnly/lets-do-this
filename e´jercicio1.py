personajes = []
FechaDeCumple = []
a=input("ingrese su nombre")
b=int(input("cuando cumples 100"))
while a!= "close":
    personajes.append(a)
    FechaDeCumple.append(b)
    a = input ("siguiente personaje")
    b = int(input ("siguiente fecha"))
def pregunta():
    
    print (personajes)
    print (FechaDeCumple)

pregunta()
    
