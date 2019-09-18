# sencill programa de xifrat i desxifrat per substitució (tipus xifrat cèsar)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : el mateix

L = 26 # nombre caràcters alfabet

def obteDespl():
# retorna un enter corresponent al desplaçament d'un simple xifrat tipus Cèsar
    desp = input("entreu un nombre natural corresponent al desplaçament: ")
    return int(desp)

def codifica(caracter, despl):
# si caràcter és lletra 'a'..'z' retorna <caracter> codificat usant <despl>
# altrament retorna caràcter tal qual
    lowerChar = caracter.lower()
    if lowerChar >= 'a' and caracter <='z':
        posZero = ord('a')
        return chr((ord(lowerChar) -posZero + despl) % L+posZero)
    else:
        return lowerChar

def descodifica(caracter, despl):
# si caràcter és lletra 'a'..'z' retorna <caracter> descodificat usant <despl>
# altrament retorna caràcter tal qual
    lowerChar = caracter.lower()
    if lowerChar >= 'a' and lowerChar <='z':
        posZero = ord('a')
        return chr((ord(lowerChar)-posZero - despl) % L + posZero)
    else:
        return lowerChar

def cesar():
# obté un desplaçament i un text, i mostra el text codificat amb mètode Cèsar (amb el desp. entrat)
# després el decodifica i mostra l'original
    desp = obteDespl()
    print("DESPLAÇAMENT: ", desp)
    text = input("entra el text que vols xifrar: ")
    text_xifrat = ""
    for k in range(len(text)):
        text_xifrat += codifica(text[k], desp)
    print("TEXT XIFRAT: ", text_xifrat)
    # ara decodificarem
    text_original = ""
    for k in range(len(text_xifrat)):
        text_original += descodifica(text_xifrat[k],desp)
    print("TEXT ORIGINAL: ", text_original)

cesar()
