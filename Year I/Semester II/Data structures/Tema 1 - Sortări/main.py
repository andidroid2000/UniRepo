import random
import time

def bubble_sort(lista):
    for i in range(len(lista)):
        ordonat = True
#verific elementele adiacente si le interschimb daca e nevoie
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                ordonat = False
#cand n-am mai avut swapp-uri, ma opresc
        if ordonat:
            return lista

def count_sort(lista):
    lista_finala = []
    frecventa = [0] * (max(lista) + 1)
#completez lista cu frecventa aparitiei elementelor din vector
    for element in lista:
        frecventa[element] = frecventa[element] + 1
#in functie de frecventa, adaug elementele intr-o noua lista
    for i in range(len(frecventa)):
        if frecventa[i] != 0:
            while frecventa[i] != 0:
                lista_finala.append(i)
                frecventa[i] = frecventa[i] - 1
    return lista_finala

def merge(lista, stanga, mijloc, dreapta):
    n1 = mijloc - stanga + 1
    n2 = dreapta - mijloc

    S = [0] * (n1)
    D = [0] * (n2)

    for i in range(0, n1):
        S[i] = lista[stanga + i]

    for j in range(0, n2):
        D[j] = lista[mijloc + j + 1]

    i = j = 0
    k = stanga
#interclasez elementele pana raman fara elem intr-un vector
    while i < n1 and j < n2:
        if S[i] <= D[j]:
            lista[k] = S[i]
            i += 1
        else:
            lista[k] = D[j]
            j += 1
        k += 1
#pentru vectorul unde mi-au ramas elementele, le adauag in lista finala
    while i < n1:
        lista[k] = S[i]
        i += 1
        k += 1

    while j < n2:
        lista[k] = D[j]
        j += 1
        k += 1

def merge_sort(lista, stanga, dreapta):
    aux = [0] * (len(lista))
    if stanga < dreapta:
        mijloc = (stanga + dreapta) // 2
        merge_sort(lista, stanga, mijloc)
        merge_sort(lista, mijloc + 1, dreapta)
#dupa ce are loc procesul de divide, iau vectorii formati si ii recombin cu ajutorul interclasarii
        merge(lista, stanga, mijloc, dreapta)
    return lista

#aleg mediana ca fiind valoarea mijlocie dintre stanga, mijloc, dreapta si o pun pe locul pivotului (dreapta)
def mediana_din_3(lista, stanga, dreapta):
    mijloc = (stanga+dreapta)//2
    if (lista[stanga] > lista[mijloc] and lista[stanga] < lista[dreapta]) or (lista[stanga] < lista[mijloc] and lista[stanga] > lista[dreapta]):
        lista[stanga], lista[dreapta] = lista[dreapta], lista[stanga]
    elif (lista[mijloc] > lista[stanga] and lista[mijloc] < lista[dreapta]) or (lista[mijloc] < lista[stanga] and lista[mijloc] > lista[dreapta]):
        lista[mijloc], lista[dreapta] = lista[dreapta], lista[mijloc]
    return lista[dreapta]

#mut elementele mai mici decat pivotul la stanga, iar la final pun pivotul dupa ultima poz pe ultima poz dupa el mai mici
def partitie(lista, stanga, dreapta):
    i = stanga - 1
    pivot = mediana_din_3(lista, stanga, dreapta)
#mut elementele mai mici
    for j in range(stanga, dreapta):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
#mut pivotul
    lista[i + 1], lista[dreapta] = lista[dreapta], lista[i + 1]
#pozitia pivotului
    return (i + 1)

def quick_sort(lista, stanga, dreapta):
    if stanga < dreapta:
#pozitie pivot
        pp = partitie(lista, stanga, dreapta)
        quick_sort(lista, stanga, pp - 1)
        quick_sort(lista, pp + 1, dreapta)
    return lista

def radix_sort(lista):

    maximul_puterii = max(lista)
    putere = 1
    while maximul_puterii / putere > 0:

        lista_noua = [0] * (len(lista))
        frecventa = [0] * (10)
#calcul frecventa lsd
        for i in range(0, len(lista)):
            index = lista[i] // putere
            frecventa[index % 10] += 1
#lista frecventa cumulata
        for i in range(1, 10):
            frecventa[i] = frecventa[i - 1] + frecventa[i]
        i = len(lista) - 1
#formare lista noua cu ajutorul frecventelor cumulate
        while i >= 0:
            index = lista[i] // putere
            lista_noua[frecventa[index % 10] - 1] = lista[i]
            frecventa[index % 10] -= 1
            i =  i-1
#transferul listei noi in lista initiala
        for i in range(0, len(lista)):
            lista[i] = lista_noua[i]
#trecerea la urmatoarea cifra din numere ( lsd - unitati, zecimale, sute etc)
        putere = putere*10

    return lista

def genereaza_lista(n, val_max):
    lista = []
    for i in range(n):
        numar = random.randint(1, val_max)
        lista.append(numar)
    return lista

def __main__():

    nr_teste = 5
    teste = [[10000, 100],[1000, 100000],[1000, 1000],[1000, 100000],[1000000, 10000]]
    for i in range(nr_teste):
        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector = bubble_sort(vector)
        print("Test", i + 1, "L-am sortat in", (time.time() - start), "secunde\n")

        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector = count_sort(vector)
        print("Test", i + 1, "L-am sortat in", (time.time() - start), "secunde\n")

        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector = merge_sort(vector, 0, len(vector)-1)
        print("Test", i + 1, "L-am sortat in", (time.time() - start), "secunde\n")

        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector = quick_sort(vector, 0, len(vector)-1)
        print("Test", i + 1, "L-am sortat in", (time.time() - start), "secunde\n")

        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector= radix_sort(vector)
        print("Test", i + 1, "L-am sortat in", (time.time() - start), "secunde\n")
        
        vector = genereaza_lista(teste[i][0], teste[i][1])
        start = time.time()
        vector.sort()
        print("Test", i+1, "L-am sortat in", (time.time() - start),"secunde\n")

__main__()
