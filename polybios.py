# sencill programa de xifrat i desxifrat per substitució (tipus xifrat polybios)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació (no s'encripten)
# alfabet text xifrat : parell de lletres alfabet anglès majúscules codificant la posicio d'una matriu

L = 26 # nombre caràcters alfabet

def construeixTaula(files,columnes):
    taula = [['0' for x in range(columnes)] for y in range(files)]
    num_lletra = 0;
    total_taula=files*columnes;
    # Es podria genererar la taula de forma més simple però:
    # S'ha de tenir en compte que hi poden haver col·lisions de lletres si la dimensió de la taula és < 26
    # També s'ha de controlar que no posi més caràcters si la taula te dimensió > 26
    for i in range(files):
        for j in range(columnes):
            if num_lletra < L:
                caracter =chr(ord('a')+num_lletra)
                if caracter == 'i' and total_taula < L:
                    taula[i][j]="ij"
                    num_lletra += 2
                else:
                    taula[i][j] = caracter
                    num_lletra += 1

    return taula


def codifica(caracter, files, columnes):
# si caràcter és lletra 'a'..'z' retorna cadena XY (X i Y son caracters A-Z) codificat usant files i columnes
# altrament retorna caràcter tal qual
    lowerChar = caracter.lower()
    posZeroRes = ord('A')
    if lowerChar >= 'a' and caracter <='z':
        posicio = ord(lowerChar) - ord('a')
        primer = posicio // columnes
        segon = posicio % columnes
        if (files * columnes) < L and caracter >= 'j':
            # si hi ha colisio (maxim 1) fem que la i i la j vagin juntes
            # hem de fer corre enrera les altres lletres 1 posicio
            segon = ((segon - 1) % columnes)
            if segon >=  (ord('j') - ord('a')) % columnes:
                # Com es colisiona la j, si la columna resultant es superior a la posicio de j:
                # hem de fer que les files tirin 1 valor enrere. per ex en un 5x5 la K seria la posicio CA, pero ha de ser BE
                primer =((primer -1) % columnes)

        return chr(posZeroRes + primer) + chr(posZeroRes + segon)
    else:
        return lowerChar

def descodifica(primer,segon, files, columnes):
# primer i segon son caracters A - Z
# retorna el caracter de descodificacio polybios tenint en compte files i columnes

    pos1 = (ord(primer) - ord('A'))*columnes
    pos2 = ord(segon) - ord('A')
    if files * columnes < L and pos2 + pos1 >=  (ord('j') - ord('a')):
        ## si hi ha colisió, a partir de la j hem de sumar 1 a tots els caracters
        pos1 +=1
    return chr(ord('a') + pos2 + pos1)


def polybios():
# obté un numero de files, un numero de columnes i un text. Mostra el text codificat amb el mètode Polybios
# després el decodifica i mostra l'original
    print("Entra un nombre de files i columnes que compleixin num_files x num_columnes >=25")
    num_files = input("Entra el nombre de files: ")
    num_columnes = input("Entra el nombra de columnes: ")
    files = int(num_files)
    cols = int(num_columnes)
    if files*cols<25:
        print("El nombre de files x nombre de columnes es inferior a 25.")
    else:
        text = input("entra el text que vols xifrar: ")
        text_xifrat = ""
        for k in range(len(text)):
            text_xifrat += codifica(text[k], files,cols)
        print("TEXT XIFRAT: ", text_xifrat)
        ## ara decodificarem
        text_original = ""
        i = 0
        while(i<len(text_xifrat)):
            if text_xifrat[i] >='A' and text_xifrat[i] <='Z':
                text_original += descodifica(text_xifrat[i],text_xifrat[i+1],files,cols)
                i +=2
            else:
                text_original += text_xifrat[i];
                i +=1
        print("TEXT ORIGINAL: ", text_original)

polybios()
