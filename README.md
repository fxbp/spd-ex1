# Exercici 1: Mètodes criptogràfics senzills

## Implementació dels mètodes criptogràfics

### Xifrat Cesar

El mètode per obtenir el xifrat és molt simple.

Donat que es treballa amb caracters de l'alfabet anglès es pot aprofitar la codificació dels caracters en ASCII.

- Primer s'obté el número del caràcter en qüestió i se li resta el número que representa el caràcter 'a'
- Un cop s'ha passat el caràcter a un número entre el 0 i el 25 s'aplica el desplaçament de forma modular (si es passa de 25 torna a començar a 0)
- Finalment s'obté el caràcter sumant el valor obtingut a al número que representa el caràcter 'a'.


Per desxifrar un caràcter es fa la mateixa operació amb 1 canvi. En comptes de sumar el desplaçament un cop obtingut el valor del caràcter entre 0 i 25, el que es fa és restar-lo. De forma que s'obté el caràcter original.

    posZero = ord('a')
    return chr((ord(lowerChar)-posZero - despl) % L + posZero)
