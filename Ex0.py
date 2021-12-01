def puissance(n,p):
    if p==0:
        return 0
    else:
        i=1
        result = n
        while i < p:
            result = result * n
            i = i + 1
        return result

print(puissance(2,5))
chaine = "BTS SIO"
taille = len(chaine)
print("taille =",taille,"initiale =",chaine[0])
for i in range(taille):
  print(chaine[i],"-",end="")  #l'option end demande de ne rien faire après le print
nombre = "324"
t=len(nombre)
print("\n taille=",t)
for car in nombre:
  print(car, "/", int(car)+2)