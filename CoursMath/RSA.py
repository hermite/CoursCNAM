# Envoi le code correspondant à la lettre en fonction de la table de codage fournie et appliquant le cryptage RSA
# # ou un espace si cela en est un
# # ou un "?" si le caractère n'est pas dans la table de codage
def cryptChar(char, tabCodage, n,c):
    if char == " ":
        return " "
    for ligne in tabCodage:
        if ligne[0] == char:
            return (int(ligne[1]) ** c) % n
    return "?"


# Envoi la lettre correspondant au code en fonction de la table de codage fournie et appliquant le décryptage RSA
# ou un espace si cela en est un
# ou un "?" si le caractère n'est pas dans la table de codage
def decryptChar(code, tabCodage,n,d):
    if code == " ":
        return " "
    codeDecrypt = (int(code) ** d) % n
    for ligne in tabCodage:
        if ligne[1] == codeDecrypt:
            return ligne[0]
    return "?"

#Crypte un message en utilisant la méthode de chiffrement RSA, une table de codage et la clé publique
def cryptChaine(chaine,tab, n, c):
        mCrypt = ""
        for char in chaine:
            mCrypt = mCrypt + str(cryptChar(char,tab,n,c)) + "|"
        return mCrypt

#Decrypte un message crypté avec la méthode de chiffrement RSA, en utilisant une table de codage et la clé privée
def decryptChaine(chaine,tab, n, d):
    mDeCrypt = ""
    codeChar = ""
    for char in chaine:
        if char == "|":
            mDeCrypt = mDeCrypt + decryptChar(codeChar, tab, n, d)
            codeChar = ""
        else:
            codeChar = codeChar + str(char)
    return mDeCrypt

#table de codage
tabCODAGE = [["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6], ["G", 7], ["H", 8], ["I", 9], ["J", 10], ["K", 11], ["L", 12], ["M", 13],
             ["N", 14], ["O", 15], ["P", 16], ["Q", 17], ["R", 18], ["S", 19], ["T", 20], ["U", 21], ["V", 22], ["W", 23], ["X", 24], ["Y", 25],
             ["Z", 26], ["a", 27], ["b", 28], ["c", 29], ["d", 30], ["e", 31], ["f", 32], ["g", 33], ["h", 34], ["i", 35], ["j", 36], ["k", 37],
             ["l", 38], ["m", 39], ["n", 40], ["o", 41], ["p", 42], ["q", 43], ["r", 44], ["s", 45], ["t", 46], ["u", 47], ["v", 48], ["w", 49],
             ["x", 50], ["y", 51], ["z", 52]]

#test de l'exercice
p=5
q=11
n=p*q
c=9
d=9
print(cryptChaine("IREMAUVERGNE",tabCODAGE,n,c))
print(decryptChaine("48|20|29|5|12|18|20|21|8|20|14|20|12|1|31|20|8|25|",tabCODAGE,n,d))


#table de codage
p2=13
q2=19
n2=p*q
c2=23
d2=9
tabCODAGE2 = [["A", 26], ["B", 39], ["C", 16], ["D", 29], ["E", 42], ["F", 6], ["G", 20], ["H", 33], ["I", 46], ["J", 23], ["K", 11], ["L", 37], ["M", 25],
             ["N", 38], ["O", 27], ["P", 40], ["Q", 41], ["R", 30], ["S", 19], ["T", 44], ["U", 45], ["V", 9], ["W", 47], ["X", 24], ["Y", 12],
             ["Z", 26], ["a", 15], ["b", 3], ["c", 17], ["d", 5], ["e", 31], ["f", 7], ["g", 8], ["h", 22], ["i", 10], ["j", 36], ["k", 49],
             ["l", 50], ["m", 51], ["n", 52], ["o", 4], ["p", 18], ["q", 43], ["r", 32], ["s", 21], ["t", 34], ["u", 35], ["v", 48], ["w", 13],
             ["x", 1], ["y", 2], ["z", 28]]
#Autre test
print(cryptChaine("Ce fut un exercice interessant",tabCODAGE2,55,9))
print(decryptChaine("48|16| |32|37|6| |37|30| |16|35|16|44|19|50|19|16| |50|30|6|16|44|16|45|45|42|30|6|",tabCODAGE,55,9))