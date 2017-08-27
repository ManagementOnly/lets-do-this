#NessBenavides

#programacion de un algoridmo que estime el maximo comun divisor
#a partir de una lista de numeros 


print ("CALCULO DEL MAXIMO COMUN DIVISOR")
print ("ingrese una lista de numeros")
print ("para calcular el valor digite close")


bolsa = []

elemento = input("elemento : ")

while elemento != "close":
    bolsa.append(int(elemento))
    elemento = input("siguiente elemento : ")
    

print ("usted ingreso los siguientes valores") , bolsa

print ("maximo ", max(bolsa))

if min(bolsa)!= 0:
    print ("minimo ", min(bolsa))
else:
    print ("MCD indefinido quitar el cero de la lista")



def SonDivisibles (num,lista):
    divisibles = True
    for i in range(len(lista)):
        if(lista[i]%num>0):
            divisibles == False
    return divisibles

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
