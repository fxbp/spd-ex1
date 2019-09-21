# sencill programa de xifrat i desxifrat per transposicio (tipus xifrat Rail Fence)
# alfabet text en clar: lletres alfabet anglès 'a'..'z' (només minúscules) + signes de puntuació
# alfabet text xifrat : el mateix


def obteRail():
# retorna un enter corresponent al rail d'un simple xifrat tipus Rail Fence
    rails = input("entreu un nombre natural corresponent al rail: ")
    return int(rails)

def obtenirNovaPosicio(posicio, rail, desp, diff, mida):
    # calcula la seguent posicio en base al nombre de num_rails
    if diff == 0:
        diff = desp
    # si diff = 0 es que som al primer o ultim rail, per tant hem de moure desp cada cop
    posicio = posicio + diff
    diff = desp-diff
    # excepte el primer i ultim rail, tots els rails tenen 2 desplaçaments:
    # el primer a desp - rail*2
    # el segon a rail*2
    # utilitza la variable diff per intercanviar aquest 2 desplaçaments
    if posicio >= mida:
        rail +=1;
        posicio = rail
        diff  = desp -2*rail

    return posicio, rail, diff

def codifica(missatge, num_rails):
# retorna el missatge xifrat tipus rail Fence utilitzant num_rails
    xifrat = [0 for x in range(len(missatge))]
    rail = 0;
    posicio = rail;
    desp = 2*num_rails -2
    # desp son les posicions que ha de desplaçar el primer rail
    diff  = 0
    for k in range(len(missatge)):
        xifrat[k]= missatge[posicio]
        posicio, rail, diff = obtenirNovaPosicio(posicio,rail, desp, diff, len(missatge))

    return "".join(str(x) for x in xifrat)

def descodifica(missatge, num_rails):
# retorna el missatge dexifrat utilitzant el metode rail Fence i num_rails
    desxifrat = [0 for x in range(len(missatge))]
    rail = 0;
    posicio = rail;
    desp = 2*num_rails -2
    # desp son les posicions que ha de desplaçar el primer rail
    diff  = 0
    for k in range(len(missatge)):
        desxifrat[posicio] = missatge[k]
        posicio, rail, diff = obtenirNovaPosicio(posicio,rail, desp, diff, len(missatge))

    return "".join(str(x) for x in desxifrat)


def railFence():
# obté un nombre de rail i un text, i mostra el text codificat amb mètode Rail Fence (amb el rail. entrat)
# després el decodifica i mostra l'original
    num_rails = obteRail()
    print("Rail: ", num_rails)
    text = input("entra el text que vols xifrar: ")
    text_xifrat = codifica(text,num_rails)
    print("TEXT XIFRAT: ", text_xifrat)
    # ara decodificarem
    text_original = descodifica(text_xifrat, num_rails)
    print("TEXT ORIGINAL: ", text_original)

railFence()

#it's the honky tonk women that gimme, gimme, gimme the honky tonk blues (honky tonk women, by the rolling stones)
