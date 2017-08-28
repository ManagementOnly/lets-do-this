#Ness Benavides
#este progama crea una lista elemento por elemento
#reporta los integros de la lista
#busca si un valor esta en la lista

lista1 = []

print ("crear lista")
elemento = input("elemento de la lista: ")

while elemento != "close":
    lista1.append(elemento)
    elemento = input("siguiente elemento ")


def funcion1():
    for elemento in lista1:
        print (elemento)

funcion1 ()

def funcion2():
    print ("largo de la lista",len(lista1))
    print ("minimo", min(lista1))
    print ("maximo", max(lista1))
    print ("elementos de la lista : ", lista1[0:len(lista1)])
    x = input("esta este valor en la lista? ")

    print (x in (lista1))

reporte = input ("reportes: ")

if reporte == "chart":
    funcion2 ()            

