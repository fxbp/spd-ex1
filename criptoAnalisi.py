
L=26
#nombre de lletres de l'alfabet

def creaTaulaFrequencia():
    taula = {
        'a': 8.16  ,'b': 1.49 , 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.28,'g': 2.01, 'h': 6.09,
        'i': 6.96,'j': 0.15,'k': 0.77,'l': 4.05,'m': 2.40, 'n': 6.74, 'o': 7.5, 'p': 1.92,
        'q': 0.09, 'r': 5.98,'s': 6.32, 't': 9.05, 'u': 2.75, 'w': 0.97,'x': 0.15, 'y':1.94, 'z':0.07
    }
    return taula

def descodificaCesar(caracter, despl):
# si caràcter és lletra 'a'..'z' retorna <caracter> descodificat usant <despl>
# altrament retorna caràcter tal qual
    lowerChar = caracter.lower()
    if lowerChar >= 'a' and lowerChar <='z':
        posZero = ord('a')
        return chr((ord(lowerChar)-posZero - despl) % L + posZero)
    else:
        return lowerChar

def analitzaCesar(text, taulaFreq):
    dict = {}
    for k in range(L):
        dict[chr(ord('a')+k)] =0
    for k in range(len(text)):
        if text[k].lower() >= 'a' and text[k].lower() <='z':
            dict[text[k]] +=1;

    maxFreq = max(dict, key=dict.get)
    sort = sorted(taulaFreq, key=taulaFreq.get, reverse=True)


    resposta = "s"
    i=0
    while i < L and (resposta == "s" or resposta =="S"):
        maxTeo = sort[i]
        i += 1
        print(maxTeo, maxFreq)
        despl = abs(ord(maxTeo)-ord(maxFreq))
        desxifrat=""
        for k in range(len(text)):
            desxifrat += descodificaCesar(text[k],despl)
        print("Desxifrat Cesar:")
        print("Provant desplaçament d = ", despl)
        print("Text desxifrat:")
        print(desxifrat)
        resposta = input("Vols provar una altre opcio? [s/n] ")
        print(k < L and (resposta == "s" or resposta =="S"))

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

def descodificaRail(missatge, num_rails):
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

def analiztaRailFence(missatge):
    test = 2
    resposta = "s"
    while (resposta == "s" or resposta =="S"):
        print("Desxifrat Rail Fence:")
        print("Prova dexifrar num_rails =", test)
        print(descodificaRail(missatge,test))
        resposta = input("Vols provar amb mes rails? [s/n]")
        test +=1

def criptoAnalisi():
    taulaFreq = creaTaulaFrequencia()
    text = input("entra el text que vols analitzar: ")
    #analitzaCesar(text,taulaFreq)
    resposta = input("Amb quin tipus de desxifrat vols provar d'analitzar? [c = cesar, r = Rail Fence, altres = finalitzar] ")
    while resposta.lower() == "c" or resposta.lower() == "r":
        if resposta.lower()=="c":
            analitzaCesar(text,taulaFreq)
        else :
            analiztaRailFence(text)
        resposta = input("Vols provar un altre tipus de desxifrat? [c = cesar, r = Rail Fence, altres = finalitzar] ")

criptoAnalisi()

# xfimr litvxl. patm tkx px ebobgz yhk? tutgwhgxw ietvxl. b znxll px dghp max lvhkx. (lahp fnlm zh hg, ur jnxxg)
