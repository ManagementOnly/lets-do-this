#NessBenavides
#universidad hispanoamericana
#programacion de un algoridmo que estime el maximo comun divisor
#a partir de una lista de numeros 


print ("CALCULO DEL MAXIMO COMUN DIVISOR")
print ("ingrese una lista de numeros")
print ("para calcular el valor digite close")


lista1 = []

elemento = input("ingrese su nombre cuando cumplira 100 : ")

while elemento != "close":
    lista1.append(int(elemento))
    elemento = input("siguiente persona : ")
    

print ("usted ingreso los siguientes valores") , bolsa
print ("MCD indefinido quitar el cero de la lista")



def SonDivisibles ():
    print (lista1)
def MCD(lista):
    minimo= min(lista)
    cont=1
    while(cont<=minimo):
        if(SonDivisibles(cont,lista)==True):
           mcdValor=cont
        cont= cont+1
    return mcdValor

def main():

    print("El MCD es:",MCD(bolsa))

main()
