#print(puissance(2,5))
#chaine = "BTS SIO"
#taille = len(chaine)
#print("taille =",taille,"initiale =",chaine[0])
#for i in range(taille):
#  print(chaine[i],"-",end="")  #l'option end demande de ne rien faire après le print
#nombre = "324"
#t=len(nombre)
#print("\n taille=",t)
#for car in nombre:
#  print(car, "/", int(car)+2)*/

def getBase10(x):
    init = str(x)
    taille = len(init)
    result = 0
    position = taille
    for i in init:
        position = position - 1
        if int(i) == 1:
            result = result + 2**(position)
    return result

def afficherBase2(x):
    valeurBase10 = x
    PMax = 0
    valeurBase2 = ""
    while valeurBase10 > 2**PMax:
        PMax = PMax +1
    while PMax >= 0:
        if 2**PMax<=valeurBase10:
            valeurBase2 = valeurBase2 + "1"
            valeurBase10 = valeurBase10 - 2**PMax
        else:
            valeurBase2 = valeurBase2 + "0"
        PMax = PMax - 1
    print(str(valeurBase2))

def getBase2(x):
    valeurBase10 = x
    PMax = 0
    valeurBase2 = ""
    while valeurBase10 > 2**PMax:
        PMax = PMax +1
    while PMax >= 0:
        if 2**PMax<=valeurBase10:
            valeurBase2 = valeurBase2 + "1"
            valeurBase10 = valeurBase10 - 2**PMax
        else:
            valeurBase2 = valeurBase2 + "0"
        PMax = PMax - 1
    return(int(valeurBase2))

print(getBase10(100))
afficherBase2(1458)
print(getBase2(1458))