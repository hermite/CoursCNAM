def TranfCharBaseHexeVers10(x):
    valeur = ord(str(x))
    if valeur < 65:
        print(x)
        return x
    else:
        print(valeur - 55)
        return valeur - 55
def TransNb10VersHexa(x):
    if len(str(x)) > 1:
        print(chr(x+55))
        return chr(x+55)
    else:
        print(x)
        return str(x)

TranfCharBaseHexeVers10("D")
TranfCharBaseHexeVers10("0")
TranfCharBaseHexeVers10(2)
TranfCharBaseHexeVers10("A")
TranfCharBaseHexeVers10("F")
TransNb10VersHexa(13)
TransNb10VersHexa(0)
TransNb10VersHexa(2)
TransNb10VersHexa(10)
TransNb10VersHexa(15)